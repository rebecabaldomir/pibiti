CREATE TABLE `licitacoes` (
  `iditemcompra` varchar(45) DEFAULT NULL,
  `datareferencia` date DEFAULT NULL,
  `cnpj` varchar(45) DEFAULT NULL,
  `poderunidade` varchar(45) DEFAULT NULL,
  `modalidade` varchar(45) DEFAULT NULL,
  `valorpreco` varchar(45) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=694 DEFAULT CHARSET=utf8;