odoo.define('pos_managed_discount.models', function(require) {
    "use strict";

    const {PosGlobalState, Order, Orderline, Payment} = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const ManagedPosGlobalState = (PosGlobalState) => class extends PosGlobalState {
		hasDiscountControl() {
		    let cashier = this.get_cashier();
		    console.log(cashier);
		    let hasControl = cashier.role=='manager'?true:false;
			return hasControl;
		}
	}
	Registries.Model.extend(PosGlobalState, ManagedPosGlobalState);
	return ManagedPosGlobalState;

});
