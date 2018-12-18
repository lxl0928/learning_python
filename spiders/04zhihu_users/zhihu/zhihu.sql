
#用户数据表
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `zhihu`
-- ----------------------------
DROP TABLE IF EXISTS `zhihu`;
CREATE TABLE `zhihu` (
  `userId` varchar(20) NOT NULL,
  `nickname` varchar(20) DEFAULT NULL,
  `word` varchar(255) DEFAULT NULL,
  `business` varchar(20) DEFAULT NULL,
  `company` varchar(20) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `school` varchar(20) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `answers` int(20) DEFAULT NULL,
  `followers` int(20) DEFAULT NULL,
  `followees` int(20) DEFAULT NULL,
  `f_url` varchar(255) DEFAULT NULL,
  `flag` int(2) DEFAULT '0',
  PRIMARY KEY (`userId`),
  UNIQUE KEY `id` (`userId`),
  KEY `flag` (`flag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
