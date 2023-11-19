--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5 (Ubuntu 15.5-1.pgdg22.04+1)
-- Dumped by pg_dump version 16.1 (Ubuntu 16.1-1.pgdg22.04+1)

-- Started on 2023-11-19 16:53:51 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE analytics;
--
-- TOC entry 3363 (class 1262 OID 16393)
-- Name: analytics; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE analytics WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';


ALTER DATABASE analytics OWNER TO postgres;

\connect analytics

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3364 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16394)
-- Name: exchange_rates; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.exchange_rates (
    id character varying,
    name character varying,
    rateusd real,
    trdate date
);


ALTER TABLE public.exchange_rates OWNER TO admin;

--
-- TOC entry 3357 (class 0 OID 16394)
-- Dependencies: 214
-- Data for Name: exchange_rates; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.exchange_rates (id, name, rateusd, trdate) FROM stdin;
BTC	bitcoin	36540.785	2023-11-19
BTC	bitcoin	36568.656	2023-11-19
BTC	bitcoin	36603.746	2023-11-19
\.


-- Completed on 2023-11-19 16:53:51 MSK

--
-- PostgreSQL database dump complete
--

