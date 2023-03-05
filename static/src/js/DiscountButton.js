odoo.define('pos_managed_discount.DiscountButton', function(require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const DiscountButton = require('pos_discount.DiscountButton');


    const ManagedDiscountButton = (DiscountButton) => class extends DiscountButton {
        /**
          * @override
          */
        async onClick() {
            var self = this;
            var maxDiscountVal = this.env.pos.config.discount_pc;
            var userGroup = this.env.pos.config.flexible_discount_group_id;



            const { confirmed, payload } = await this.showPopup('NumberPopup',{
                title: 'Discount Percentage',
                startingValue: this.env.pos.config.discount_pc,
                isInputSelected: true
            });
            if (confirmed) {
                let hasDiscountControl = self.env.pos.hasDiscountControl();


                console.log('hasDiscountControl:',hasDiscountControl);


                const val = Math.round(Math.max(0,Math.min(100,parseFloat(payload))));
                if(!hasDiscountControl && val>maxDiscountVal){
                    await this.showPopup("ErrorPopup", {
                    title: "Discount Error",
                    body: "You are not allowed to set discount percentage more than "
                        + maxDiscountVal+
                        "%. Pls contact your administrator"
                    });
                    return;
                }
                await self.apply_discount(val);
            }
        }

    }

    Registries.Component.extend(DiscountButton,ManagedDiscountButton);

    return ManagedDiscountButton;
});
