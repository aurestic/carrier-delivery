
FR"DHL"
?
${to_ascii(picking.partner_id.name)}
${to_ascii(picking.partner_id.mobile or picking.partner_id.phone or '')}
${"{}, {}".format(to_ascii(picking.partner_id.street), to_ascii(picking.partner_id.street2 or '')) }
${to_ascii(picking.partner_id.city or '')}
${to_ascii(picking.partner_id.zip or '')}
${facility_code}
${shipment_ref}
${picking.number_of_packages}
${to_ascii(picking.picking_type_id.warehouse_id.partner_id.name)}
<%doc>CARACTERISTICASENVIO</%doc>
${inboundsort}<%doc>INBOUNDSORT A (Aereo) M (Maritimo) si es Canarias o Azores</%doc>
${to_ascii(destination_country)}
${to_ascii(picking.name.replace('/', '-') or '')}
${picking.carrier_id.carrier_file_id.dhl_account_code}
<%doc>OUTBOUNDSORT</%doc>


SPAIN
${picking.picking_type_id.warehouse_id.partner_id.zip}
${"{}, {}".format(to_ascii(picking.picking_type_id.warehouse_id.partner_id.street), to_ascii(picking.picking_type_id.warehouse_id.partner_id.street2 or '')) }
${to_ascii(picking.picking_type_id.warehouse_id.partner_id.city)}
${routing_code}
${legible_routing_code}
${licence_plate_code}
${legible_licence_plate_code}
${picking.picking_type_id.warehouse_id.partner_id.country_id.id != picking.partner_id.country_id.id and "CMR" or ''}
ECONOMY SELECT

${int(picking.weight)}
${pickup_date}
SERVICE AREA



ESI

1
001
P${str(picking.number_of_packages).zfill(3)}

