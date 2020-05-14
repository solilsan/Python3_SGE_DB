-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-05-2020 a las 14:56:19
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `basedatossge`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) COLLATE utf8mb4_bin NOT NULL,
  `direccion` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `telefono` varchar(9) COLLATE utf8mb4_bin NOT NULL,
  `control` varchar(255) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `telefono`, `control`) VALUES
(1, 'CompraMuchoMas', 'Calle Inventada Nª4', '965748324', '<button onclick=\"modificar(1)\" class=\"btn btn btn-outline-warning\" type=\"button\">Modificar</button><button onclick=\"borrar(1)\" class=\"btn btn btn-outline-danger mt-2\" type=\"button\">Borrar</button>');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `id` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `id_proveedor` int(11) NOT NULL,
  `cantidad` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `precio` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `total` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `control` varchar(255) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id`, `nombre`) VALUES
(1, 'inventario'),
(2, 'compras'),
(3, 'ventas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historicocompras`
--

CREATE TABLE `historicocompras` (
  `id` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `id_proveedor` int(11) NOT NULL,
  `cantidad` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `precio` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `total` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `fecha` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `nombrep` varchar(25) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `historicocompras`
--

INSERT INTO `historicocompras` (`id`, `id_producto`, `id_proveedor`, `cantidad`, `precio`, `total`, `fecha`, `nombrep`) VALUES
(1, 1, 1, '20', '1$', '20$', '14/5/2020', 'Queso'),
(2, 1, 1, '20', '1$', '20$', '14/5/2020', 'Queso'),
(3, 2, 1, '10', '2$', '20$', '14/5/2020', 'Arroz'),
(4, 2, 1, '20', '2$', '40$', '14/5/2020', 'Arroz'),
(5, 2, 1, '1', '2$', '2$', '14/5/2020', 'Arroz'),
(6, 2, 1, '1', '2$', '2$', '14/5/2020', 'Arroz'),
(7, 2, 1, '8', '2$', '16$', '14/5/2020', 'Arroz'),
(8, 1, 1, '10', '1$', '10$', '14/5/2020', 'Queso');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarios`
--

CREATE TABLE `inventarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) COLLATE utf8mb4_bin NOT NULL,
  `tipo` varchar(25) COLLATE utf8mb4_bin NOT NULL,
  `cantidad` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `precio_compra` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `precio_venta` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `control` varchar(255) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `inventarios`
--

INSERT INTO `inventarios` (`id`, `nombre`, `tipo`, `cantidad`, `precio_compra`, `precio_venta`, `control`) VALUES
(1, 'Queso', 'Lácteo', '50', '1$', '2$', '<button onclick=\"modificar(1)\" class=\"btn btn btn-outline-warning\" type=\"button\">Modificar</button><button onclick=\"borrar(1)\" class=\"btn btn btn-outline-danger mt-2\" type=\"button\">Borrar</button>'),
(2, 'Arroz', 'Comida', '240', '2$', '3$', '<button onclick=\"modificar(2)\" class=\"btn btn btn-outline-warning\" type=\"button\">Modificar</button><button onclick=\"borrar(2)\" class=\"btn btn btn-outline-danger mt-2\" type=\"button\">Borrar</button>\r\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) COLLATE utf8mb4_bin NOT NULL,
  `direccion` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `telefono` varchar(9) COLLATE utf8mb4_bin NOT NULL,
  `control` varchar(255) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`id`, `nombre`, `direccion`, `telefono`, `control`) VALUES
(1, 'VendeMucho', 'Calle Inventada Nº3', '657483923', '<button onclick=\"modificar(1)\" class=\"btn btn btn-outline-warning\" type=\"button\">Modificar</button><button onclick=\"borrar(1)\" class=\"btn btn btn-outline-danger mt-2\" type=\"button\">Borrar</button>');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) COLLATE utf8mb4_bin NOT NULL,
  `pass` varchar(30) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `pass`) VALUES
(1, 'alex', '123'),
(2, 'pepe', '123'),
(3, 'juan', '123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usudepart`
--

CREATE TABLE `usudepart` (
  `id_departamento` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `usudepart`
--

INSERT INTO `usudepart` (`id_departamento`, `id_usuario`) VALUES
(1, 1),
(2, 1),
(3, 1),
(2, 2),
(3, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `cantidad` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `precio` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `total` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `control` varchar(255) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `id_producto`, `id_cliente`, `cantidad`, `precio`, `total`, `control`) VALUES
(1, 1, 1, '10', '2$', '20$', '<button onclick=\"vender(1)\" class=\"btn btn btn-outline-warning\" type=\"button\">Vender</button><button onclick=\"borrar(1)\" class=\"btn btn btn-outline-danger mt-2\" type=\"button\">Borrar</button>\r\n');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_compra` (`id_producto`),
  ADD KEY `proveedor_compra` (`id_proveedor`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `historicocompras`
--
ALTER TABLE `historicocompras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_hc` (`id_producto`),
  ADD KEY `proveedor_hc` (`id_proveedor`);

--
-- Indices de la tabla `inventarios`
--
ALTER TABLE `inventarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usudepart`
--
ALTER TABLE `usudepart`
  ADD KEY `usu` (`id_usuario`),
  ADD KEY `depart` (`id_departamento`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_venta` (`id_producto`),
  ADD KEY `cliente_venta` (`id_cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `historicocompras`
--
ALTER TABLE `historicocompras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `inventarios`
--
ALTER TABLE `inventarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `producto_compra` FOREIGN KEY (`id_producto`) REFERENCES `inventarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `proveedor_compra` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `historicocompras`
--
ALTER TABLE `historicocompras`
  ADD CONSTRAINT `producto_hc` FOREIGN KEY (`id_producto`) REFERENCES `inventarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `proveedor_hc` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usudepart`
--
ALTER TABLE `usudepart`
  ADD CONSTRAINT `depart` FOREIGN KEY (`id_departamento`) REFERENCES `departamentos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `usu` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `cliente_venta` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_venta` FOREIGN KEY (`id_producto`) REFERENCES `inventarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
