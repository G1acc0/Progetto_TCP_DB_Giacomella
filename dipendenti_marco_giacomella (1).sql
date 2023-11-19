-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 19, 2023 alle 15:18
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
-- Struttura della tabella `dipendenti_marco_giacomella`
--

CREATE TABLE `dipendenti_marco_giacomella` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `indirizzo` varchar(1024) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `mail` varchar(30) NOT NULL,
  `password` varchar(10) NOT NULL,
  `dataass` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `dipendenti_marco_giacomella`
--

INSERT INTO `dipendenti_marco_giacomella` (`id`, `nome`, `indirizzo`, `telefono`, `mail`, `password`, `dataass`) VALUES
(2, 'Mario', 'Regno dei funghi 1', '333 456 789', 'mario.brothers@funghi.com', 'peaches', '1986-02-21'),
(3, 'Luigi', 'Regno dei funghi 1', '333 654 987', 'luigi.brothers@funghi.com', 'fungo', '1986-01-10'),
(4, 'Joseph', 'Via conte francesco', '567 889 355', 'joseph.brothers@funghi.com', 'amon', '1999-07-12'),
(5, 'Majimbo', 'via pizza 7', '123 666 777', 'majimmbo.brothers@funghi.com', 'chan', '1980-04-12'),
(6, 'Ken', 'via barbie 4', '212 212 333', 'ken.brothers@funghi', 'mojodojo', '2000-02-24');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_marco_giacomella`
--
ALTER TABLE `dipendenti_marco_giacomella`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_marco_giacomella`
--
ALTER TABLE `dipendenti_marco_giacomella`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
