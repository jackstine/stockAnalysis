/*Selects the list of companies that are in the list of companies that 
have ^ in at least one of their symbols*/
select * from NasdaqCompanyListing where symbol NOT LIKE ("%^%") AND name IN (select DISTINCT(name) from NasdaqCompanyListing where symbol IN (select symbol from NasdaqListingReference where symbol LIKE ("%^%")));

/*Selects all the companies that do not have a regular symbol and only have a ^ in there symbol*/
select * from NasdaqCompanyListing where symbol LIKE("%^%") AND name NOT IN (select DISTINCT(name) from NasdaqCompanyListing where symbol NOT LIKE ("%^%") AND name IN (select DISTINCT(name) from NasdaqCompanyListing where symbol IN (select symbol from NasdaqListingReference where symbol LIKE ("%^%"))));



(('ALP^O', 'Alabama Power Company', None)
('BDN^E', 'Brandywine Realty Tr', None)
('BGE^B', 'Baltimore Gas & Electric Company', None)
('BIR^A', 'Berkshire Income Realty, Inc.', None)
('CFC^A', 'Countrywide Financial Corporation', None)
('CFC^B', 'Countrywide Financial Corporation', None)
('COF^P', 'Capital One Financial Corp', None)
('DTLA^', 'Brookfield DTLA Inc.', None)
('EP^C', 'El Paso Corporation', None)
('FBS^A', 'First Banks, Inc.', None)
('FNB^E', 'F.N.B. Corporation', None)
('GPE^A', 'Georgia Power Company', None)
('HLM^', 'Hillman Group Capital Trust', None)
('HSFC^B', 'Household Finance Corp', None)
('HUSI^F', 'HSBC USA, Inc.', None)
('HUSI^G', 'HSBC USA, Inc.', None)
('HUSI^H', 'HSBC USA, Inc.', None)
('IPL^D', 'Interstate Power and Light Company', None)
('IVR^A', 'Invesco Mortgage Capital Inc.', None)
('MP^D', 'Mississippi Power Company', None)
('NMK^B', 'Niagara Mohawk Holdings, Inc.', None)
('NMK^C', 'Niagara Mohawk Holdings, Inc.', None)
('NW^C', 'Natl Westminster Pfd', None)
('PL^C', 'Protective Life Corporation', None)
('PL^E', 'Protective Life Corporation', None)
('SCE^B', 'Southern California Edison Company', None)
('SCE^C', 'Southern California Edison Company', None)
('SCE^D', 'Southern California Edison Company', None)
('SCE^E', 'Southern California Edison Company', None)
('SCE^F', 'Southern California Edison Company', None)
('SCE^G', 'Southern California Edison Company', None)
('SCE^H', 'Southern California Edison Company', None)
('SOV^C', 'Santander Holdings USA, Inc.', None))
