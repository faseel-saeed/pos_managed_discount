odoo.define('pos_managed_discount.models', function(require) {
    "use strict";

    const {PosGlobalState, Order, Orderline, Payment} = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const ManagedPosGlobalState = (PosGlobalState) => class extends PosGlobalState {
		hasDiscountControl() {
		    let user = this.get_user();
		    //console.log(cashier);
		    let hasControl = user.discount_admin==true?true:false;
			return hasControl;
		}

		get_user() {
            return this.user;
        }
	}
	Registries.Model.extend(PosGlobalState, ManagedPosGlobalState);
	return ManagedPosGlobalState;

});
