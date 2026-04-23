--
-- PostgreSQL database dump
--

\restrict ef5OI4OPEEftcgYFzD4BSLkPkHJUDkDJ5r2xvqYhUJRmnTaTusx5fkofNHIMjGm

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

-- Started on 2026-04-23 21:24:34

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 35318)
-- Name: clients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clients (
    id integer NOT NULL,
    client_code character varying(50) NOT NULL,
    name character varying(200) NOT NULL
);


ALTER TABLE public.clients OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 35321)
-- Name: clients_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clients_id_seq OWNER TO postgres;

--
-- TOC entry 4854 (class 0 OID 0)
-- Dependencies: 218
-- Name: clients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clients_id_seq OWNED BY public.clients.id;


--
-- TOC entry 219 (class 1259 OID 35322)
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    order_number character varying(50) NOT NULL,
    supplier_id integer,
    product_code character varying(50) NOT NULL,
    quantity integer NOT NULL,
    unit_price double precision NOT NULL,
    total_amount double precision NOT NULL,
    order_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    expected_delivery timestamp without time zone,
    status character varying(20),
    user_id integer
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 35326)
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.orders_id_seq OWNER TO postgres;

--
-- TOC entry 4855 (class 0 OID 0)
-- Dependencies: 220
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- TOC entry 221 (class 1259 OID 35327)
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    is_folder boolean DEFAULT false,
    parent_id integer,
    code character varying(50) NOT NULL,
    descr character varying(200),
    article character varying(100),
    measure character varying(20),
    nds_rate double precision
);


ALTER TABLE public.products OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 35331)
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_id_seq OWNER TO postgres;

--
-- TOC entry 4856 (class 0 OID 0)
-- Dependencies: 222
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- TOC entry 223 (class 1259 OID 35337)
-- Name: suppliers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.suppliers (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    contact_person character varying(100),
    phone character varying(20),
    email character varying(100),
    address text
);


ALTER TABLE public.suppliers OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 35342)
-- Name: suppliers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.suppliers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.suppliers_id_seq OWNER TO postgres;

--
-- TOC entry 4857 (class 0 OID 0)
-- Dependencies: 224
-- Name: suppliers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.suppliers_id_seq OWNED BY public.suppliers.id;


--
-- TOC entry 225 (class 1259 OID 35343)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(80) NOT NULL,
    email character varying(120) NOT NULL,
    password_hash character varying(200) NOT NULL,
    full_name character varying(150),
    role character varying(50),
    is_active boolean DEFAULT true,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 35350)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 4858 (class 0 OID 0)
-- Dependencies: 226
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 4661 (class 2604 OID 35351)
-- Name: clients id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clients ALTER COLUMN id SET DEFAULT nextval('public.clients_id_seq'::regclass);


--
-- TOC entry 4662 (class 2604 OID 35352)
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- TOC entry 4664 (class 2604 OID 35353)
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- TOC entry 4666 (class 2604 OID 35355)
-- Name: suppliers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.suppliers ALTER COLUMN id SET DEFAULT nextval('public.suppliers_id_seq'::regclass);


--
-- TOC entry 4667 (class 2604 OID 35356)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 4839 (class 0 OID 35318)
-- Dependencies: 217
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.clients (id, client_code, name) VALUES (1, 'C001', 'ООО Альфа');
INSERT INTO public.clients (id, client_code, name) VALUES (2, 'C002', 'ООО Бета');
INSERT INTO public.clients (id, client_code, name) VALUES (3, 'C003', 'ООО Гамма');


--
-- TOC entry 4841 (class 0 OID 35322)
-- Dependencies: 219
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (1, 'ORD-20260324-1', 1, 'P001', 8, 100, 800, '2026-03-24 10:00:00', '2026-03-29 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (2, 'ORD-20260324-2', 2, 'P002', 9, 120, 1080, '2026-03-24 12:00:00', '2026-03-29 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (3, 'ORD-20260324-3', 3, 'P003', 10, 140, 1400, '2026-03-24 14:00:00', '2026-03-29 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (4, 'ORD-20260325-1', 1, 'P004', 11, 160, 1760, '2026-03-25 10:00:00', '2026-03-30 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (5, 'ORD-20260325-2', 2, 'P005', 12, 180, 2160, '2026-03-25 12:00:00', '2026-03-30 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (6, 'ORD-20260325-3', 3, 'P006', 8, 200, 1600, '2026-03-25 14:00:00', '2026-03-30 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (7, 'ORD-20260326-1', 1, 'P007', 9, 220, 1980, '2026-03-26 10:00:00', '2026-03-31 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (8, 'ORD-20260326-2', 2, 'P008', 10, 240, 2400, '2026-03-26 12:00:00', '2026-03-31 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (9, 'ORD-20260326-3', 3, 'P001', 11, 260, 2860, '2026-03-26 14:00:00', '2026-03-31 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (10, 'ORD-20260327-1', 1, 'P002', 12, 280, 3360, '2026-03-27 10:00:00', '2026-04-01 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (11, 'ORD-20260327-2', 2, 'P003', 8, 300, 2400, '2026-03-27 12:00:00', '2026-04-01 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (12, 'ORD-20260327-3', 3, 'P004', 9, 320, 2880, '2026-03-27 14:00:00', '2026-04-01 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (13, 'ORD-20260328-1', 1, 'P005', 10, 340, 3400, '2026-03-28 10:00:00', '2026-04-02 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (14, 'ORD-20260328-2', 2, 'P006', 11, 360, 3960, '2026-03-28 12:00:00', '2026-04-02 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (15, 'ORD-20260328-3', 3, 'P007', 12, 380, 4560, '2026-03-28 14:00:00', '2026-04-02 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (16, 'ORD-20260329-1', 1, 'P008', 8, 400, 3200, '2026-03-29 10:00:00', '2026-04-03 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (17, 'ORD-20260329-2', 2, 'P001', 9, 420, 3780, '2026-03-29 12:00:00', '2026-04-03 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (18, 'ORD-20260329-3', 3, 'P002', 10, 440, 4400, '2026-03-29 14:00:00', '2026-04-03 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (19, 'ORD-20260330-1', 1, 'P003', 11, 460, 5060, '2026-03-30 10:00:00', '2026-04-04 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (20, 'ORD-20260330-2', 2, 'P004', 12, 480, 5760, '2026-03-30 12:00:00', '2026-04-04 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (21, 'ORD-20260330-3', 3, 'P005', 8, 500, 4000, '2026-03-30 14:00:00', '2026-04-04 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (22, 'ORD-20260331-1', 1, 'P006', 9, 520, 4680, '2026-03-31 10:00:00', '2026-04-05 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (23, 'ORD-20260331-2', 2, 'P007', 10, 540, 5400, '2026-03-31 12:00:00', '2026-04-05 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (24, 'ORD-20260331-3', 3, 'P008', 11, 560, 6160, '2026-03-31 14:00:00', '2026-04-05 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (25, 'ORD-20260401-1', 1, 'P001', 12, 580, 6960, '2026-04-01 10:00:00', '2026-04-06 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (26, 'ORD-20260401-2', 2, 'P002', 8, 600, 4800, '2026-04-01 12:00:00', '2026-04-06 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (27, 'ORD-20260401-3', 3, 'P003', 9, 620, 5580, '2026-04-01 14:00:00', '2026-04-06 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (28, 'ORD-20260402-1', 1, 'P004', 10, 640, 6400, '2026-04-02 10:00:00', '2026-04-07 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (29, 'ORD-20260402-2', 2, 'P005', 11, 660, 7260, '2026-04-02 12:00:00', '2026-04-07 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (30, 'ORD-20260402-3', 3, 'P006', 12, 680, 8160, '2026-04-02 14:00:00', '2026-04-07 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (31, 'ORD-20260403-1', 1, 'P007', 8, 700, 5600, '2026-04-03 10:00:00', '2026-04-08 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (32, 'ORD-20260403-2', 2, 'P008', 9, 720, 6480, '2026-04-03 12:00:00', '2026-04-08 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (33, 'ORD-20260403-3', 3, 'P001', 10, 740, 7400, '2026-04-03 14:00:00', '2026-04-08 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (34, 'ORD-20260404-1', 1, 'P002', 11, 760, 8360, '2026-04-04 10:00:00', '2026-04-09 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (35, 'ORD-20260404-2', 2, 'P003', 12, 780, 9360, '2026-04-04 12:00:00', '2026-04-09 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (36, 'ORD-20260404-3', 3, 'P004', 8, 800, 6400, '2026-04-04 14:00:00', '2026-04-09 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (37, 'ORD-20260405-1', 1, 'P005', 9, 820, 7380, '2026-04-05 10:00:00', '2026-04-10 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (38, 'ORD-20260405-2', 2, 'P006', 10, 840, 8400, '2026-04-05 12:00:00', '2026-04-10 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (39, 'ORD-20260405-3', 3, 'P007', 11, 860, 9460, '2026-04-05 14:00:00', '2026-04-10 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (40, 'ORD-20260406-1', 1, 'P008', 12, 880, 10560, '2026-04-06 10:00:00', '2026-04-11 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (41, 'ORD-20260406-2', 2, 'P001', 8, 900, 7200, '2026-04-06 12:00:00', '2026-04-11 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (42, 'ORD-20260406-3', 3, 'P002', 9, 920, 8280, '2026-04-06 14:00:00', '2026-04-11 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (43, 'ORD-20260407-1', 1, 'P003', 10, 940, 9400, '2026-04-07 10:00:00', '2026-04-12 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (44, 'ORD-20260407-2', 2, 'P004', 11, 960, 10560, '2026-04-07 12:00:00', '2026-04-12 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (45, 'ORD-20260407-3', 3, 'P005', 12, 980, 11760, '2026-04-07 14:00:00', '2026-04-12 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (46, 'ORD-20260408-1', 1, 'P006', 8, 1000, 8000, '2026-04-08 10:00:00', '2026-04-13 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (47, 'ORD-20260408-2', 2, 'P007', 9, 1020, 9180, '2026-04-08 12:00:00', '2026-04-13 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (48, 'ORD-20260408-3', 3, 'P008', 10, 1040, 10400, '2026-04-08 14:00:00', '2026-04-13 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (49, 'ORD-20260409-1', 1, 'P001', 11, 1060, 11660, '2026-04-09 10:00:00', '2026-04-14 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (50, 'ORD-20260409-2', 2, 'P002', 12, 1080, 12960, '2026-04-09 12:00:00', '2026-04-14 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (51, 'ORD-20260409-3', 3, 'P003', 8, 1100, 8800, '2026-04-09 14:00:00', '2026-04-14 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (52, 'ORD-20260410-1', 1, 'P004', 9, 1120, 10080, '2026-04-10 10:00:00', '2026-04-15 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (53, 'ORD-20260410-2', 2, 'P005', 10, 1140, 11400, '2026-04-10 12:00:00', '2026-04-15 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (54, 'ORD-20260410-3', 3, 'P006', 11, 1160, 12760, '2026-04-10 14:00:00', '2026-04-15 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (55, 'ORD-20260411-1', 1, 'P007', 12, 1180, 14160, '2026-04-11 10:00:00', '2026-04-16 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (56, 'ORD-20260411-2', 2, 'P008', 8, 1200, 9600, '2026-04-11 12:00:00', '2026-04-16 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (57, 'ORD-20260411-3', 3, 'P001', 9, 1220, 10980, '2026-04-11 14:00:00', '2026-04-16 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (58, 'ORD-20260412-1', 1, 'P002', 10, 1240, 12400, '2026-04-12 10:00:00', '2026-04-17 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (59, 'ORD-20260412-2', 2, 'P003', 11, 1260, 13860, '2026-04-12 12:00:00', '2026-04-17 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (60, 'ORD-20260412-3', 3, 'P004', 12, 1280, 15360, '2026-04-12 14:00:00', '2026-04-17 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (61, 'ORD-20260413-1', 1, 'P005', 8, 1300, 10400, '2026-04-13 10:00:00', '2026-04-18 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (62, 'ORD-20260413-2', 2, 'P006', 9, 1320, 11880, '2026-04-13 12:00:00', '2026-04-18 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (63, 'ORD-20260413-3', 3, 'P007', 10, 1340, 13400, '2026-04-13 14:00:00', '2026-04-18 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (64, 'ORD-20260414-1', 1, 'P008', 11, 1360, 14960, '2026-04-14 10:00:00', '2026-04-19 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (65, 'ORD-20260414-2', 2, 'P001', 12, 1380, 16560, '2026-04-14 12:00:00', '2026-04-19 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (66, 'ORD-20260414-3', 3, 'P002', 8, 1400, 11200, '2026-04-14 14:00:00', '2026-04-19 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (67, 'ORD-20260415-1', 1, 'P003', 9, 1420, 12780, '2026-04-15 10:00:00', '2026-04-20 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (68, 'ORD-20260415-2', 2, 'P004', 10, 1440, 14400, '2026-04-15 12:00:00', '2026-04-20 00:00:00', 'pending', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (69, 'ORD-20260415-3', 3, 'P005', 11, 1460, 16060, '2026-04-15 14:00:00', '2026-04-20 00:00:00', 'delivered', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (70, 'ORD-20260416-1', 1, 'P006', 12, 1480, 17760, '2026-04-16 10:00:00', '2026-04-21 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (71, 'ORD-20260416-2', 2, 'P007', 8, 1500, 12000, '2026-04-16 12:00:00', '2026-04-21 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (72, 'ORD-20260416-3', 3, 'P008', 9, 1520, 13680, '2026-04-16 14:00:00', '2026-04-21 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (73, 'ORD-20260417-1', 1, 'P001', 10, 1540, 15400, '2026-04-17 10:00:00', '2026-04-22 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (74, 'ORD-20260417-2', 2, 'P002', 11, 1560, 17160, '2026-04-17 12:00:00', '2026-04-22 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (75, 'ORD-20260417-3', 3, 'P003', 12, 1580, 18960, '2026-04-17 14:00:00', '2026-04-22 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (76, 'ORD-20260418-1', 1, 'P004', 8, 1600, 12800, '2026-04-18 10:00:00', '2026-04-23 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (77, 'ORD-20260418-2', 2, 'P005', 9, 1620, 14580, '2026-04-18 12:00:00', '2026-04-23 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (78, 'ORD-20260418-3', 3, 'P006', 10, 1640, 16400, '2026-04-18 14:00:00', '2026-04-23 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (79, 'ORD-20260419-1', 1, 'P007', 11, 1660, 18260, '2026-04-19 10:00:00', '2026-04-24 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (80, 'ORD-20260419-2', 2, 'P008', 12, 1680, 20160, '2026-04-19 12:00:00', '2026-04-24 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (81, 'ORD-20260419-3', 3, 'P001', 8, 1700, 13600, '2026-04-19 14:00:00', '2026-04-24 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (82, 'ORD-20260420-1', 1, 'P002', 9, 1720, 15480, '2026-04-20 10:00:00', '2026-04-25 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (83, 'ORD-20260420-2', 2, 'P003', 10, 1740, 17400, '2026-04-20 12:00:00', '2026-04-25 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (84, 'ORD-20260420-3', 3, 'P004', 11, 1760, 19360, '2026-04-20 14:00:00', '2026-04-25 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (85, 'ORD-20260421-1', 1, 'P005', 12, 1780, 21360, '2026-04-21 10:00:00', '2026-04-26 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (86, 'ORD-20260421-2', 2, 'P006', 8, 1800, 14400, '2026-04-21 12:00:00', '2026-04-26 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (87, 'ORD-20260421-3', 3, 'P007', 9, 1820, 16380, '2026-04-21 14:00:00', '2026-04-26 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (88, 'ORD-20260422-1', 1, 'P008', 10, 1840, 18400, '2026-04-22 10:00:00', '2026-04-27 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (89, 'ORD-20260422-2', 2, 'P001', 11, 1860, 20460, '2026-04-22 12:00:00', '2026-04-27 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (90, 'ORD-20260422-3', 3, 'P002', 12, 1880, 22560, '2026-04-22 14:00:00', '2026-04-27 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (91, 'ORD-20260423-1', 1, 'P003', 8, 1900, 15200, '2026-04-23 10:00:00', '2026-04-28 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (92, 'ORD-20260423-2', 2, 'P004', 9, 1920, 17280, '2026-04-23 12:00:00', '2026-04-28 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (93, 'ORD-20260423-3', 3, 'P005', 10, 1940, 19400, '2026-04-23 14:00:00', '2026-04-28 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (94, 'ORD-20260424-1', 1, 'P006', 11, 1960, 21560, '2026-04-24 10:00:00', '2026-04-29 00:00:00', 'shipped', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (95, 'ORD-20260424-2', 2, 'P007', 12, 1980, 23760, '2026-04-24 12:00:00', '2026-04-29 00:00:00', 'processing', 1);
INSERT INTO public.orders (id, order_number, supplier_id, product_code, quantity, unit_price, total_amount, order_date, expected_delivery, status, user_id) VALUES (96, 'ORD-20260424-3', 3, 'P008', 8, 2000, 16000, '2026-04-24 14:00:00', '2026-04-29 00:00:00', 'shipped', 1);


--
-- TOC entry 4843 (class 0 OID 35327)
-- Dependencies: 221
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (1, false, NULL, 'P001', 'Ноутбук Dell XPS 13', 'DX13-001', 'шт', 20);
INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (2, false, NULL, 'P002', 'Клавиатура Keychron K6 механическая', 'KK6-002', 'шт', 20);
INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (3, false, NULL, 'P003', 'Мышь Logitech MX Master 3 беспроводная', 'LMX3-003', 'шт', 20);
INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (4, false, NULL, 'P004', 'Монитор LG UltraFine 27 дюймов', 'LG27-004', 'шт', 20);
INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (5, false, NULL, 'P005', 'Внешний SSD Samsung T7 1TB', 'ST7-005', 'шт', 20);
INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (6, false, NULL, 'P006', 'USB-C хаб Anker 7-в-1', 'ANK7-006', 'шт', 20);
INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (7, false, NULL, 'P007', 'Веб-камера Logitech C920', 'LC920-007', 'шт', 20);
INSERT INTO public.products (id, is_folder, parent_id, code, descr, article, measure, nds_rate) VALUES (8, false, NULL, 'P008', 'Кресло офисное Ergonomic Pro', 'ECP-008', 'шт', 20);


--
-- TOC entry 4845 (class 0 OID 35337)
-- Dependencies: 223
-- Data for Name: suppliers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.suppliers (id, name, contact_person, phone, email, address) VALUES (1, 'ООО ТехСнаб', 'Иван Петров', '+79001234567', 'petrov@techsnab.ru', 'г. Краснодар');
INSERT INTO public.suppliers (id, name, contact_person, phone, email, address) VALUES (2, 'ООО Глобал Девайс', 'Алексей Смирнов', '+79001234568', 'smirnov@globaldevice.ru', 'г. Краснодар');
INSERT INTO public.suppliers (id, name, contact_person, phone, email, address) VALUES (3, 'ООО Хардвер Плюс', 'Дмитрий Иванов', '+79001234569', 'ivanov@hardwareplus.ru', 'г. Краснодар');


--
-- TOC entry 4847 (class 0 OID 35343)
-- Dependencies: 225
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, username, email, password_hash, full_name, role, is_active, created_at) VALUES (1, 'admin', 'admin@example.com', 'hash1', 'Администратор', 'admin', true, '2026-01-01 00:00:00');
INSERT INTO public.users (id, username, email, password_hash, full_name, role, is_active, created_at) VALUES (2, 'manager', 'manager@example.com', 'hash2', 'Менеджер склада', 'manager', true, '2026-01-10 00:00:00');


--
-- TOC entry 4859 (class 0 OID 0)
-- Dependencies: 218
-- Name: clients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clients_id_seq', 3, true);


--
-- TOC entry 4860 (class 0 OID 0)
-- Dependencies: 220
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 3, true);


--
-- TOC entry 4861 (class 0 OID 0)
-- Dependencies: 222
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 3, true);


--
-- TOC entry 4862 (class 0 OID 0)
-- Dependencies: 224
-- Name: suppliers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.suppliers_id_seq', 2, true);


--
-- TOC entry 4863 (class 0 OID 0)
-- Dependencies: 226
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- TOC entry 4671 (class 2606 OID 35358)
-- Name: clients clients_client_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_client_code_key UNIQUE (client_code);


--
-- TOC entry 4673 (class 2606 OID 35360)
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (id);


--
-- TOC entry 4675 (class 2606 OID 35362)
-- Name: orders orders_order_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_order_number_key UNIQUE (order_number);


--
-- TOC entry 4677 (class 2606 OID 35364)
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- TOC entry 4679 (class 2606 OID 35366)
-- Name: products products_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_code_key UNIQUE (code);


--
-- TOC entry 4681 (class 2606 OID 35368)
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- TOC entry 4683 (class 2606 OID 35372)
-- Name: suppliers suppliers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.suppliers
    ADD CONSTRAINT suppliers_pkey PRIMARY KEY (id);


--
-- TOC entry 4685 (class 2606 OID 35374)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 4687 (class 2606 OID 35376)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 4689 (class 2606 OID 35378)
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- TOC entry 4690 (class 2606 OID 35379)
-- Name: orders orders_product_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_product_code_fkey FOREIGN KEY (product_code) REFERENCES public.products(code) ON DELETE CASCADE;


--
-- TOC entry 4691 (class 2606 OID 35384)
-- Name: orders orders_supplier_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_supplier_id_fkey FOREIGN KEY (supplier_id) REFERENCES public.suppliers(id) ON DELETE SET NULL;


--
-- TOC entry 4692 (class 2606 OID 35389)
-- Name: orders orders_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE SET NULL;


--
-- TOC entry 4693 (class 2606 OID 35394)
-- Name: products products_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES public.products(id) ON DELETE SET NULL;


-- Completed on 2026-04-23 21:24:34

--
-- PostgreSQL database dump complete
--

\unrestrict ef5OI4OPEEftcgYFzD4BSLkPkHJUDkDJ5r2xvqYhUJRmnTaTusx5fkofNHIMjGm

