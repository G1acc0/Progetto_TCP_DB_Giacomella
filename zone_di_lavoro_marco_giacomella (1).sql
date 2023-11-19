-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 19, 2023 alle 15:19
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `progetto`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_marco_giacomella`
--

CREATE TABLE `zone_di_lavoro_marco_giacomella` (
  `idzona` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `num_clienti` int(11) NOT NULL,
  `coddip` int(11) NOT NULL,
  `settore_che_seguono` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zone_di_lavoro_marco_giacomella`
--

INSERT INTO `zone_di_lavoro_marco_giacomella` (`idzona`, `nome`, `num_clienti`, `coddip`, `settore_che_seguono`) VALUES
(1, 'reggio', 10000, 5, 'Ospedali'),
(2, 'fosdondo', 1000, 6, 'Costruzioni'),
(3, 'fabbrico', 100, 2, 'Agricolo'),
(4, 'Capri', 20000, 3, 'Agricolo'),
(5, 'Milano', 300000, 4, 'Fashion');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zone_di_lavoro_marco_giacomella`
--
ALTER TABLE `zone_di_lavoro_marco_giacomella`
  ADD PRIMARY KEY (`idzona`),
  ADD KEY `coddip` (`coddip`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_marco_giacomella`
--
ALTER TABLE `zone_di_lavoro_marco_giacomella`
  MODIFY `idzona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zone_di_lavoro_marco_giacomella`
--
ALTER TABLE `zone_di_lavoro_marco_giacomella`
  ADD CONSTRAINT `zone_di_lavoro_marco_giacomella_ibfk_1` FOREIGN KEY (`coddip`) REFERENCES `dipendenti_marco_giacomella` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
