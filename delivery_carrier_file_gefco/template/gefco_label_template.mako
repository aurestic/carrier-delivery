^XA

^FX Cabecera
^CF0,130
^FO50,50^FDGEFCO^FS
^CFC,20
^FO400,50^FD${to_ascii(picking.carrier_id.partner_id.city or '')}^FS
^FO720,50^FD${to_ascii(picking.carrier_id.carrier_file_id.gefco_agency_code or '')}^FS
^FO400,75^FDTel: ${picking.carrier_id.partner_id.phone or ''}^FS
^FO400,100^FDFax: ${picking.carrier_id.partner_id.fax or ''}^FS
^FO50,140^GB700,1,3^FS

^FX Nombre y direccion expedidor
^CF0,30
^FO50,170^FDExp:^FS
^CFA,40
^FO120,150^FD${to_ascii(wh_address.name)}^FS
^CFA,20
^FO120,190^FD${to_ascii(wh_address.street)} ${to_ascii(wh_address.street2 or '')}^FS
^CFA,40
^FO50,210^FD${to_ascii(wh_address.country_id.code)}^FS
^CFA,30
^FO120,215^FD${to_ascii(wh_address.zip)} ${to_ascii(wh_address.city)}^FS
^FO50,250^GB700,1,3^FS

^FX Nombre y direccion destinatario
^CF0,30
^FO50,280^FDDest:^FS
^CF0,50
^FO120,270^FD${to_ascii(picking.partner_id.name)}^FS
^CF0,30
^FO120,310^FD${to_ascii(picking.partner_id.street)} ${to_ascii(picking.partner_id.street2 or '')}^FS
^CF0,40
^FO50,340^FD${to_ascii(picking.partner_id.country_id.code)}^FS
^CF0,50
^FO120,340^FD${to_ascii(picking.partner_id.zip)}^FS
^FO270,340^FD${to_ascii(picking.partner_id.city)}^FS
^FO50,380^GB700,1,3^FS

^FX Codigo de barras
^CF0,30
^BY6,2.5,80
^FO120,400^BCN^FD${barcode_ref}^FS

^FO50,560^GB700,1,3^FS
^CF0,20
^FO50,570^FDColis: ${package_number}/${total_packages}^FS
^FO220,570^FDRecep:^FS
^FO290,570^FD${gefco_configuration.gefco_shipper_id}^FS
^FO610,570^FDEdite le:^FS
^FO680,570^FD${pickup_date}^FS
^FO50,590^FDPoids: ${weight}^FS
^FO220,590^FDRef. client:^FS
^FO290,590^FD${gefco_configuration.gefco_shipper_id}^FS
^FO610,590^FDA livrer le:^FS
^FO680,590^FD^FS
^FO50,610^GB700,1,3^FS

^CFA,180,40
^FO50,630^FD${to_ascii(directional_destination_code)}^FS
^CF0,80,50
^FO590,650^FD${to_ascii(destination_code)}^FS
^XZ