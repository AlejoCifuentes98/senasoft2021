-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-10-2021 a las 20:00:57
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cardbug`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add partida', 7, 'add_partida'),
(26, 'Can change partida', 7, 'change_partida'),
(27, 'Can delete partida', 7, 'delete_partida'),
(28, 'Can view partida', 7, 'view_partida'),
(29, 'Can add registro', 8, 'add_registro'),
(30, 'Can change registro', 8, 'change_registro'),
(31, 'Can delete registro', 8, 'delete_registro'),
(32, 'Can view registro', 8, 'view_registro'),
(33, 'Can add turno', 9, 'add_turno'),
(34, 'Can change turno', 9, 'change_turno'),
(35, 'Can delete turno', 9, 'delete_turno'),
(36, 'Can view turno', 9, 'view_turno'),
(37, 'Can add tablero', 10, 'add_tablero'),
(38, 'Can change tablero', 10, 'change_tablero'),
(39, 'Can delete tablero', 10, 'delete_tablero'),
(40, 'Can view tablero', 10, 'view_tablero'),
(41, 'Can add tipo', 11, 'add_tipo'),
(42, 'Can change tipo', 11, 'change_tipo'),
(43, 'Can delete tipo', 11, 'delete_tipo'),
(44, 'Can view tipo', 11, 'view_tipo'),
(45, 'Can add cartas', 12, 'add_cartas'),
(46, 'Can change cartas', 12, 'change_cartas'),
(47, 'Can delete cartas', 12, 'delete_cartas'),
(48, 'Can view cartas', 12, 'view_cartas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$cjVwL5iZlOctD2YhFLRZ29$zr40rnW/jWHQIRKuR0rYgTP7InK72SGenxpdEJ+1yCo=', '2021-10-22 17:55:26.486220', 1, 'admin', '', '', '', 1, 1, '2021-10-22 17:04:53.285984'),
(2, 'pbkdf2_sha256$260000$IjpxQOfHCyqaHqKFsmHjBh$55y99ISxQYHZ9YoPQ0TG+FyQCX3wgAuqImu0YhMCmqo=', '2021-10-22 17:54:12.424878', 0, 'mario', '', '', '', 1, 1, '2021-10-22 17:11:45.144524'),
(3, 'pbkdf2_sha256$260000$GHIcD58hs9XbbN0sRBUySK$X+hT8abso1nngWdkYYebGjQY4IJp2ua+o/DN6DLMUoU=', NULL, 0, 'alejo', '', '', '', 1, 1, '2021-10-22 17:17:34.185057'),
(4, 'pbkdf2_sha256$260000$9DUqvScFEiGzQAOW6n0ax7$16GQof02LbSkV4CUl02a3w8EFHQOZteIgj/1PQA6J34=', NULL, 0, 'alejo2', '', '', '', 1, 1, '2021-10-22 17:17:55.140550'),
(5, 'pbkdf2_sha256$260000$1B8S1k3792biVZfuO3m1XV$EiIyfbAy0MYHi9wgi+DOH1Jr8Qym7TcgADjdz9bRrM0=', NULL, 0, 'mario2', '', '', '', 1, 1, '2021-10-22 17:18:15.293123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cartas_cartas`
--

CREATE TABLE `cartas_cartas` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(80) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `tipo_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cartas_cartas`
--

INSERT INTO `cartas_cartas` (`id`, `nombre`, `imagen`, `tipo_id`) VALUES
(1, 'Pedro', 'cards/AvatarMaker_11lVXjI.png', 1),
(2, 'Juan', 'cards/AvatarMaker_5_DsVb89F.png', 1),
(3, 'Carlos', 'cards/AvatarMaker_4_QAtDVBs.png', 1),
(4, 'Juanita', 'cards/AvatarMaker_2_1W9c7CZ.png', 1),
(5, 'Antonio', 'cards/AvatarMaker_3_A38ysRy.png', 1),
(6, 'Carolina', 'cards/AvatarMaker_1_OxfCFSD.png', 1),
(7, 'Desarrolladores', 'cards/avatars_K25Xwwm.jpg', 1),
(8, 'Nomina', 'cards/2_luJ30pw.jpg', 2),
(9, 'Facturacion', 'cards/im3-6_2mxpKOD.jpg', 2),
(10, 'Recibos', 'cards/4_vZuR7NK.jpg', 2),
(11, 'Comprobante contable', 'cards/3_dHKnIeb.png', 2),
(12, 'Usuarios', 'cards/5_AiI8OeF.jpg', 2),
(13, 'Contabilidad', 'cards/6_nK2XMwR.png', 2),
(14, '404', 'cards/1_ocDDtgK.png', 3),
(15, 'Stack overflow', 'cards/6_AiG4hns.png', 3),
(16, 'Memory out range', 'cards/6_A4uEs8s.png', 3),
(17, 'Null', 'cards/3_rBuIEvo.png', 3),
(18, 'Syntaxis error', 'cards/2_uSlZhO2.png', 3),
(19, 'Encoding error', 'cards/4_I8OPDxE.png', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cartas_tipo`
--

CREATE TABLE `cartas_tipo` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cartas_tipo`
--

INSERT INTO `cartas_tipo` (`id`, `nombre`) VALUES
(1, 'desarrollador'),
(2, 'modulo'),
(3, 'error');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-10-22 17:08:05.172184', '1', 'desarrollador', 1, '[{\"added\": {}}]', 11, 1),
(2, '2021-10-22 17:08:13.921727', '2', 'modulo', 1, '[{\"added\": {}}]', 11, 1),
(3, '2021-10-22 17:08:36.036082', '3', 'error', 1, '[{\"added\": {}}]', 11, 1),
(4, '2021-10-22 17:09:08.534309', '1', 'Pedro', 1, '[{\"added\": {}}]', 12, 1),
(5, '2021-10-22 17:09:23.398970', '2', 'Juan', 1, '[{\"added\": {}}]', 12, 1),
(6, '2021-10-22 17:09:38.833613', '3', 'Carlos', 1, '[{\"added\": {}}]', 12, 1),
(7, '2021-10-22 17:09:53.146702', '4', 'Juanita', 1, '[{\"added\": {}}]', 12, 1),
(8, '2021-10-22 17:10:22.347318', '5', 'Antonio', 1, '[{\"added\": {}}]', 12, 1),
(9, '2021-10-22 17:10:44.841559', '6', 'Carolina', 1, '[{\"added\": {}}]', 12, 1),
(10, '2021-10-22 17:11:04.639555', '7', 'Desarrolladores', 1, '[{\"added\": {}}]', 12, 1),
(11, '2021-10-22 17:20:06.033229', '2', 'alejo e320f jugador 2', 1, '[{\"added\": {}}]', 8, 1),
(12, '2021-10-22 17:20:17.095479', '3', 'alejo2 e320f jugador 3', 1, '[{\"added\": {}}]', 8, 1),
(13, '2021-10-22 17:20:27.094116', '4', 'mario2 e320f jugador 4', 1, '[{\"added\": {}}]', 8, 1),
(14, '2021-10-22 17:23:26.517314', '8', 'Nomina', 1, '[{\"added\": {}}]', 12, 1),
(15, '2021-10-22 17:23:44.900700', '9', 'Facturacion', 1, '[{\"added\": {}}]', 12, 1),
(16, '2021-10-22 17:24:04.517119', '10', 'Recibos', 1, '[{\"added\": {}}]', 12, 1),
(17, '2021-10-22 17:24:34.412719', '11', 'Comprobante contable', 1, '[{\"added\": {}}]', 12, 1),
(18, '2021-10-22 17:24:51.342474', '12', 'Usuarios', 1, '[{\"added\": {}}]', 12, 1),
(19, '2021-10-22 17:25:12.212258', '13', 'Contabilidad', 1, '[{\"added\": {}}]', 12, 1),
(20, '2021-10-22 17:25:29.584320', '14', '404', 1, '[{\"added\": {}}]', 12, 1),
(21, '2021-10-22 17:25:52.229983', '15', 'Stack overflow', 1, '[{\"added\": {}}]', 12, 1),
(22, '2021-10-22 17:26:20.341759', '16', 'Memory out range', 1, '[{\"added\": {}}]', 12, 1),
(23, '2021-10-22 17:26:41.157821', '17', 'Null', 1, '[{\"added\": {}}]', 12, 1),
(24, '2021-10-22 17:27:11.230055', '18', 'Syntaxis error', 1, '[{\"added\": {}}]', 12, 1),
(25, '2021-10-22 17:27:33.003125', '19', 'Encoding error', 1, '[{\"added\": {}}]', 12, 1),
(26, '2021-10-22 17:51:52.227911', '19', 'Encoding error', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(27, '2021-10-22 17:55:42.068361', '18', 'Syntaxis error', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(28, '2021-10-22 17:55:50.699673', '17', 'Null', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(29, '2021-10-22 17:55:58.271547', '16', 'Memory out range', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(30, '2021-10-22 17:56:04.335003', '14', '404', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(31, '2021-10-22 17:56:15.197465', '13', 'Contabilidad', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(32, '2021-10-22 17:56:59.470048', '7', 'Desarrolladores', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(33, '2021-10-22 17:57:21.860664', '1', 'Pedro', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(34, '2021-10-22 17:57:28.350670', '2', 'Juan', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(35, '2021-10-22 17:57:41.335823', '3', 'Carlos', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(36, '2021-10-22 17:57:57.471519', '4', 'Juanita', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(37, '2021-10-22 17:58:04.631994', '5', 'Antonio', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(38, '2021-10-22 17:58:22.942827', '8', 'Nomina', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(39, '2021-10-22 17:58:31.572457', '9', 'Facturacion', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(40, '2021-10-22 17:58:38.690858', '10', 'Recibos', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(41, '2021-10-22 17:58:46.147701', '11', 'Comprobante contable', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(42, '2021-10-22 17:59:01.374583', '12', 'Usuarios', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(43, '2021-10-22 17:59:08.833599', '13', 'Contabilidad', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(44, '2021-10-22 17:59:26.487556', '15', 'Stack overflow', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(45, '2021-10-22 17:59:33.061902', '14', '404', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(46, '2021-10-22 17:59:40.847223', '16', 'Memory out range', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(47, '2021-10-22 17:59:50.695393', '16', 'Memory out range', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(48, '2021-10-22 17:59:56.562510', '17', 'Null', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(49, '2021-10-22 18:00:04.415859', '18', 'Syntaxis error', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1),
(50, '2021-10-22 18:00:11.125815', '19', 'Encoding error', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 12, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(12, 'cartas', 'cartas'),
(11, 'cartas', 'tipo'),
(5, 'contenttypes', 'contenttype'),
(7, 'partida', 'partida'),
(8, 'partida', 'registro'),
(10, 'partida', 'tablero'),
(9, 'partida', 'turno'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-10-22 17:01:17.520344'),
(2, 'auth', '0001_initial', '2021-10-22 17:01:17.787571'),
(3, 'admin', '0001_initial', '2021-10-22 17:01:17.858154'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-10-22 17:01:17.871155'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-10-22 17:01:17.881818'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-10-22 17:01:17.917730'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-10-22 17:01:17.948151'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-10-22 17:01:17.965147'),
(9, 'auth', '0004_alter_user_username_opts', '2021-10-22 17:01:17.973148'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-10-22 17:01:17.997773'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-10-22 17:01:18.000773'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-10-22 17:01:18.010775'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-10-22 17:01:18.028779'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-10-22 17:01:18.048773'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-10-22 17:01:18.062774'),
(16, 'auth', '0011_update_proxy_permissions', '2021-10-22 17:01:18.074281'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-10-22 17:01:18.085365'),
(18, 'cartas', '0001_initial', '2021-10-22 17:01:18.125486'),
(19, 'partida', '0001_initial', '2021-10-22 17:01:18.325849'),
(20, 'sessions', '0001_initial', '2021-10-22 17:01:18.351373');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('bzxemj9f8p6qh9ynwn6vs89vqezf8me5', '.eJxVjEEOwiAQRe_C2hAYmQZcuvcMBJhBqgaS0q4a764kXeju57-XtwsftrX4rfPiZxIXocXp94shPbkOQI9Q702mVtdljnIo8qBd3hrx63q4f4ESehlZc2bUEzg2kBkQiCdlKSSwjjIwUlDw3RpddGhMtJgpstOkjMbkxPsD0Ng3fQ:1mdylK:StnqvzYZlI7xl8LcwyqvUDSq4hFq388WVGNWSRl0UFk', '2021-11-05 17:55:26.488218'),
('z7b73z2gyh80j7fcnwkvvoe374yw6nlw', '.eJxVjEEOwiAQRe_C2hAYmQZcuvcMBJhBqgaS0q4a764kXeju57-XtwsftrX4rfPiZxIXocXp94shPbkOQI9Q702mVtdljnIo8qBd3hrx63q4f4ESehlZc2bUEzg2kBkQiCdlKSSwjjIwUlDw3RpddGhMtJgpstOkjMbkxPsD0Ng3fQ:1mdyhQ:Jkczju4BNSRsz7u9Y_70YAN7g_D-qWhMFcDWrXIsusk', '2021-11-05 17:51:24.586378');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partida_partida`
--

CREATE TABLE `partida_partida` (
  `id` bigint(20) NOT NULL,
  `codigo_ingreso` varchar(5) NOT NULL,
  `carta_des` int(10) UNSIGNED DEFAULT NULL CHECK (`carta_des` >= 0),
  `carta_mod` int(10) UNSIGNED DEFAULT NULL CHECK (`carta_mod` >= 0),
  `carta_err` int(10) UNSIGNED DEFAULT NULL CHECK (`carta_err` >= 0),
  `estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `partida_partida`
--

INSERT INTO `partida_partida` (`id`, `codigo_ingreso`, `carta_des`, `carta_mod`, `carta_err`, `estado`) VALUES
(1, 'e320f', 3, 9, 17, 'activa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partida_registro`
--

CREATE TABLE `partida_registro` (
  `id` bigint(20) NOT NULL,
  `jugador_numero` varchar(20) NOT NULL,
  `cartas` varchar(20) DEFAULT NULL,
  `jugador_id` int(11) NOT NULL,
  `partida_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `partida_registro`
--

INSERT INTO `partida_registro` (`id`, `jugador_numero`, `cartas`, `jugador_id`, `partida_id`) VALUES
(1, 'jugador 1', '[2, 16, 10, 18]', 2, 1),
(2, 'jugador 2', '[13, 7, 19, 11]', 3, 1),
(3, 'jugador 3', '[8, 6, 15, 4]', 4, 1),
(4, 'jugador 4', '[5, 12, 14, 1]', 5, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partida_tablero`
--

CREATE TABLE `partida_tablero` (
  `id` bigint(20) NOT NULL,
  `carta_des_1` varchar(50) DEFAULT NULL,
  `carta_des_2` varchar(50) DEFAULT NULL,
  `carta_des_3` varchar(50) DEFAULT NULL,
  `carta_des_4` varchar(50) DEFAULT NULL,
  `carta_des_5` varchar(50) DEFAULT NULL,
  `carta_des_6` varchar(50) DEFAULT NULL,
  `carta_des_7` varchar(50) DEFAULT NULL,
  `carta_mod_1` varchar(50) DEFAULT NULL,
  `carta_mod_2` varchar(50) DEFAULT NULL,
  `carta_mod_3` varchar(50) DEFAULT NULL,
  `carta_mod_4` varchar(50) DEFAULT NULL,
  `carta_mod_5` varchar(50) DEFAULT NULL,
  `carta_mod_6` varchar(50) DEFAULT NULL,
  `carta_err_1` varchar(50) DEFAULT NULL,
  `carta_err_2` varchar(50) DEFAULT NULL,
  `carta_err_3` varchar(50) DEFAULT NULL,
  `carta_err_4` varchar(50) DEFAULT NULL,
  `carta_err_5` varchar(50) DEFAULT NULL,
  `carta_err_6` varchar(50) DEFAULT NULL,
  `registro_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `partida_tablero`
--

INSERT INTO `partida_tablero` (`id`, `carta_des_1`, `carta_des_2`, `carta_des_3`, `carta_des_4`, `carta_des_5`, `carta_des_6`, `carta_des_7`, `carta_mod_1`, `carta_mod_2`, `carta_mod_3`, `carta_mod_4`, `carta_mod_5`, `carta_mod_6`, `carta_err_1`, `carta_err_2`, `carta_err_3`, `carta_err_4`, `carta_err_5`, `carta_err_6`, `registro_id`) VALUES
(1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1),
(2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2),
(3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3),
(4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4),
(5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1),
(6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2),
(7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3),
(8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4),
(9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1),
(10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2),
(11, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3),
(12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4),
(13, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1),
(14, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2),
(15, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3),
(16, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partida_turno`
--

CREATE TABLE `partida_turno` (
  `id` bigint(20) NOT NULL,
  `carta_des` varchar(20) NOT NULL,
  `carta_mod` varchar(20) NOT NULL,
  `carta_err` varchar(20) NOT NULL,
  `carta_correcta` int(10) UNSIGNED DEFAULT NULL CHECK (`carta_correcta` >= 0),
  `respuesta_jugador_1` int(10) UNSIGNED DEFAULT NULL CHECK (`respuesta_jugador_1` >= 0),
  `respuesta_jugador_2` int(10) UNSIGNED DEFAULT NULL CHECK (`respuesta_jugador_2` >= 0),
  `respuesta_jugador_3` int(10) UNSIGNED DEFAULT NULL CHECK (`respuesta_jugador_3` >= 0),
  `jugador_pregunta` int(10) UNSIGNED NOT NULL CHECK (`jugador_pregunta` >= 0),
  `jugador_responde` int(10) UNSIGNED NOT NULL CHECK (`jugador_responde` >= 0),
  `tipo` varchar(20) NOT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `jugador` varchar(50) DEFAULT NULL,
  `registro_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `cartas_cartas`
--
ALTER TABLE `cartas_cartas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cartas_cartas_tipo_id_79a8376c_fk_cartas_tipo_id` (`tipo_id`);

--
-- Indices de la tabla `cartas_tipo`
--
ALTER TABLE `cartas_tipo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `partida_partida`
--
ALTER TABLE `partida_partida`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `partida_registro`
--
ALTER TABLE `partida_registro`
  ADD PRIMARY KEY (`id`),
  ADD KEY `partida_registro_jugador_id_01649e69_fk_auth_user_id` (`jugador_id`),
  ADD KEY `partida_registro_partida_id_c67b1b71_fk_partida_partida_id` (`partida_id`);

--
-- Indices de la tabla `partida_tablero`
--
ALTER TABLE `partida_tablero`
  ADD PRIMARY KEY (`id`),
  ADD KEY `partida_tablero_registro_id_41fafe33_fk_partida_registro_id` (`registro_id`);

--
-- Indices de la tabla `partida_turno`
--
ALTER TABLE `partida_turno`
  ADD PRIMARY KEY (`id`),
  ADD KEY `partida_turno_registro_id_1e5d1b01_fk_partida_registro_id` (`registro_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cartas_cartas`
--
ALTER TABLE `cartas_cartas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `cartas_tipo`
--
ALTER TABLE `cartas_tipo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `partida_partida`
--
ALTER TABLE `partida_partida`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `partida_registro`
--
ALTER TABLE `partida_registro`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `partida_tablero`
--
ALTER TABLE `partida_tablero`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `partida_turno`
--
ALTER TABLE `partida_turno`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `cartas_cartas`
--
ALTER TABLE `cartas_cartas`
  ADD CONSTRAINT `cartas_cartas_tipo_id_79a8376c_fk_cartas_tipo_id` FOREIGN KEY (`tipo_id`) REFERENCES `cartas_tipo` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `partida_registro`
--
ALTER TABLE `partida_registro`
  ADD CONSTRAINT `partida_registro_jugador_id_01649e69_fk_auth_user_id` FOREIGN KEY (`jugador_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `partida_registro_partida_id_c67b1b71_fk_partida_partida_id` FOREIGN KEY (`partida_id`) REFERENCES `partida_partida` (`id`);

--
-- Filtros para la tabla `partida_tablero`
--
ALTER TABLE `partida_tablero`
  ADD CONSTRAINT `partida_tablero_registro_id_41fafe33_fk_partida_registro_id` FOREIGN KEY (`registro_id`) REFERENCES `partida_registro` (`id`);

--
-- Filtros para la tabla `partida_turno`
--
ALTER TABLE `partida_turno`
  ADD CONSTRAINT `partida_turno_registro_id_1e5d1b01_fk_partida_registro_id` FOREIGN KEY (`registro_id`) REFERENCES `partida_registro` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
