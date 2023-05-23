--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Ubuntu 15.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 15.3 (Ubuntu 15.3-1.pgdg20.04+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: agendamento; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.agendamento (
    idagendamento integer NOT NULL,
    dataagendamento date NOT NULL,
    codservico_id integer NOT NULL,
    idcliente_id integer NOT NULL,
    idveiculo_id integer NOT NULL
);


ALTER TABLE public.agendamento OWNER TO concessionaria;

--
-- Name: agendamento_idagendamento_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.agendamento ALTER COLUMN idagendamento ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.agendamento_idagendamento_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO concessionaria;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO concessionaria;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO concessionaria;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO concessionaria;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO concessionaria;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO concessionaria;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: cliente; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.cliente (
    idcliente integer NOT NULL,
    nome character varying(100) NOT NULL,
    endereco character varying(100) NOT NULL,
    telefone character varying(14) NOT NULL,
    email character varying(50) NOT NULL,
    ehflamengo boolean NOT NULL,
    ehotaku boolean NOT NULL,
    ehsousa boolean NOT NULL
);


ALTER TABLE public.cliente OWNER TO concessionaria;

--
-- Name: cliente_idcliente_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.cliente ALTER COLUMN idcliente ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.cliente_idcliente_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO concessionaria;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO concessionaria;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO concessionaria;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO concessionaria;

--
-- Name: funcionario; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.funcionario (
    idfuncionario integer NOT NULL,
    nome character varying(100) NOT NULL,
    codcargo character varying(20) NOT NULL,
    salario double precision NOT NULL,
    dataadmissao date NOT NULL
);


ALTER TABLE public.funcionario OWNER TO concessionaria;

--
-- Name: funcionario_idfuncionario_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.funcionario ALTER COLUMN idfuncionario ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.funcionario_idfuncionario_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: servico; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.servico (
    idservico integer NOT NULL,
    codservico character varying(20) NOT NULL,
    valorservico double precision NOT NULL,
    dataservico date NOT NULL,
    idveiculo_id integer NOT NULL
);


ALTER TABLE public.servico OWNER TO concessionaria;

--
-- Name: servico_idservico_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.servico ALTER COLUMN idservico ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.servico_idservico_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: veiculo; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.veiculo (
    idveiculo integer NOT NULL,
    valor double precision NOT NULL,
    codmarca character varying(20) NOT NULL,
    numportas character varying(1) NOT NULL,
    ano character varying(4) NOT NULL,
    modelo character varying(30) NOT NULL,
    cor character varying(20) NOT NULL
);


ALTER TABLE public.veiculo OWNER TO concessionaria;

--
-- Name: veiculo_idveiculo_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.veiculo ALTER COLUMN idveiculo ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.veiculo_idveiculo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: venda; Type: TABLE; Schema: public; Owner: concessionaria
--

CREATE TABLE public.venda (
    idvenda integer NOT NULL,
    datavenda date NOT NULL,
    valorvenda double precision NOT NULL,
    idcliente_id integer NOT NULL,
    idveiculo_id integer NOT NULL
);


ALTER TABLE public.venda OWNER TO concessionaria;

--
-- Name: venda_idvenda_seq; Type: SEQUENCE; Schema: public; Owner: concessionaria
--

ALTER TABLE public.venda ALTER COLUMN idvenda ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.venda_idvenda_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: agendamento; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.agendamento (idagendamento, dataagendamento, codservico_id, idcliente_id, idveiculo_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add cliente	7	add_cliente
26	Can change cliente	7	change_cliente
27	Can delete cliente	7	delete_cliente
28	Can view cliente	7	view_cliente
29	Can add funcionario	8	add_funcionario
30	Can change funcionario	8	change_funcionario
31	Can delete funcionario	8	delete_funcionario
32	Can view funcionario	8	view_funcionario
33	Can add veiculo	9	add_veiculo
34	Can change veiculo	9	change_veiculo
35	Can delete veiculo	9	delete_veiculo
36	Can view veiculo	9	view_veiculo
37	Can add venda	10	add_venda
38	Can change venda	10	change_venda
39	Can delete venda	10	delete_venda
40	Can view venda	10	view_venda
41	Can add servico	11	add_servico
42	Can change servico	11	change_servico
43	Can delete servico	11	delete_servico
44	Can view servico	11	view_servico
45	Can add agendamento	12	add_agendamento
46	Can change agendamento	12	change_agendamento
47	Can delete agendamento	12	delete_agendamento
48	Can view agendamento	12	view_agendamento
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$600000$S5SUndOKKNrNw0ZGPseswu$kgbOfUfZMBY3zq2F4pcTHJ0Kl7YMuVZzYwnQwJmBSwA=	\N	t	admin				t	t	2023-05-23 11:25:58.471983-03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.cliente (idcliente, nome, endereco, telefone, email, ehflamengo, ehotaku, ehsousa) FROM stdin;
1	John Smith	123 Main St	123-456-7890	john.smith@example.com	t	f	f
2	Alice Johnson	456 Elm St	987-654-3210	alice.johnson@example.com	f	t	f
3	Michael Davis	789 Oak St	555-555-5555	michael.davis@example.com	f	t	f
4	Emily Wilson	321 Pine St	111-222-3333	emily.wilson@example.com	f	f	t
5	Daniel Brown	567 Cedar St	444-444-4444	daniel.brown@example.com	t	f	f
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	app	cliente
8	app	funcionario
9	app	veiculo
10	app	venda
11	app	servico
12	app	agendamento
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-05-23 11:25:38.205067-03
2	auth	0001_initial	2023-05-23 11:25:38.279205-03
3	admin	0001_initial	2023-05-23 11:25:38.307493-03
4	admin	0002_logentry_remove_auto_add	2023-05-23 11:25:38.317935-03
5	admin	0003_logentry_add_action_flag_choices	2023-05-23 11:25:38.330029-03
6	app	0001_initial	2023-05-23 11:25:38.394424-03
7	contenttypes	0002_remove_content_type_name	2023-05-23 11:25:38.420647-03
8	auth	0002_alter_permission_name_max_length	2023-05-23 11:25:38.432765-03
9	auth	0003_alter_user_email_max_length	2023-05-23 11:25:38.444892-03
10	auth	0004_alter_user_username_opts	2023-05-23 11:25:38.456587-03
11	auth	0005_alter_user_last_login_null	2023-05-23 11:25:38.468633-03
12	auth	0006_require_contenttypes_0002	2023-05-23 11:25:38.472799-03
13	auth	0007_alter_validators_add_error_messages	2023-05-23 11:25:38.48529-03
14	auth	0008_alter_user_username_max_length	2023-05-23 11:25:38.502148-03
15	auth	0009_alter_user_last_name_max_length	2023-05-23 11:25:38.515164-03
16	auth	0010_alter_group_name_max_length	2023-05-23 11:25:38.528612-03
17	auth	0011_update_proxy_permissions	2023-05-23 11:25:38.544507-03
18	auth	0012_alter_user_first_name_max_length	2023-05-23 11:25:38.555522-03
19	sessions	0001_initial	2023-05-23 11:25:38.571486-03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: funcionario; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.funcionario (idfuncionario, nome, codcargo, salario, dataadmissao) FROM stdin;
\.


--
-- Data for Name: servico; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.servico (idservico, codservico, valorservico, dataservico, idveiculo_id) FROM stdin;
\.


--
-- Data for Name: veiculo; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.veiculo (idveiculo, valor, codmarca, numportas, ano, modelo, cor) FROM stdin;
1	25000	1	4	2021	Civic	Preto
2	30000	1	4	2022	Accord	Branco
3	22000	1	4	2020	City	Vermelho
4	28000	1	4	2021	Fit	Azul
5	35000	1	4	2023	CR-V	Prata
6	27000	1	4	2022	HR-V	Cinza
7	28000	1	4	2022	Civic Type R	Amarelo
8	24000	1	4	2020	Pilot	Verde
9	26000	1	4	2021	Odyssey	Laranja
10	32000	1	4	2023	Ridgeline	Roxo
\.


--
-- Data for Name: venda; Type: TABLE DATA; Schema: public; Owner: concessionaria
--

COPY public.venda (idvenda, datavenda, valorvenda, idcliente_id, idveiculo_id) FROM stdin;
\.


--
-- Name: agendamento_idagendamento_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.agendamento_idagendamento_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: cliente_idcliente_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.cliente_idcliente_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 19, true);


--
-- Name: funcionario_idfuncionario_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.funcionario_idfuncionario_seq', 1, false);


--
-- Name: servico_idservico_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.servico_idservico_seq', 1, false);


--
-- Name: veiculo_idveiculo_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.veiculo_idveiculo_seq', 1, false);


--
-- Name: venda_idvenda_seq; Type: SEQUENCE SET; Schema: public; Owner: concessionaria
--

SELECT pg_catalog.setval('public.venda_idvenda_seq', 1, false);


--
-- Name: agendamento agendamento_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (idagendamento);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (idcliente);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (idfuncionario);


--
-- Name: servico servico_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.servico
    ADD CONSTRAINT servico_pkey PRIMARY KEY (idservico);


--
-- Name: veiculo veiculo_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.veiculo
    ADD CONSTRAINT veiculo_pkey PRIMARY KEY (idveiculo);


--
-- Name: venda venda_pkey; Type: CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT venda_pkey PRIMARY KEY (idvenda);


--
-- Name: agendamento_codservico_id_1d68dcdf; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX agendamento_codservico_id_1d68dcdf ON public.agendamento USING btree (codservico_id);


--
-- Name: agendamento_idcliente_id_d1fd958f; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX agendamento_idcliente_id_d1fd958f ON public.agendamento USING btree (idcliente_id);


--
-- Name: agendamento_idveiculo_id_68c16f15; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX agendamento_idveiculo_id_68c16f15 ON public.agendamento USING btree (idveiculo_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: servico_idveiculo_id_90e84737; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX servico_idveiculo_id_90e84737 ON public.servico USING btree (idveiculo_id);


--
-- Name: venda_idcliente_id_fefacf3f; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX venda_idcliente_id_fefacf3f ON public.venda USING btree (idcliente_id);


--
-- Name: venda_idveiculo_id_9c435c4f; Type: INDEX; Schema: public; Owner: concessionaria
--

CREATE INDEX venda_idveiculo_id_9c435c4f ON public.venda USING btree (idveiculo_id);


--
-- Name: agendamento agendamento_codservico_id_1d68dcdf_fk_servico_idservico; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_codservico_id_1d68dcdf_fk_servico_idservico FOREIGN KEY (codservico_id) REFERENCES public.servico(idservico) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: agendamento agendamento_idcliente_id_d1fd958f_fk_cliente_idcliente; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_idcliente_id_d1fd958f_fk_cliente_idcliente FOREIGN KEY (idcliente_id) REFERENCES public.cliente(idcliente) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: agendamento agendamento_idveiculo_id_68c16f15_fk_veiculo_idveiculo; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_idveiculo_id_68c16f15_fk_veiculo_idveiculo FOREIGN KEY (idveiculo_id) REFERENCES public.veiculo(idveiculo) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: servico servico_idveiculo_id_90e84737_fk_veiculo_idveiculo; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.servico
    ADD CONSTRAINT servico_idveiculo_id_90e84737_fk_veiculo_idveiculo FOREIGN KEY (idveiculo_id) REFERENCES public.veiculo(idveiculo) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: venda venda_idcliente_id_fefacf3f_fk_cliente_idcliente; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT venda_idcliente_id_fefacf3f_fk_cliente_idcliente FOREIGN KEY (idcliente_id) REFERENCES public.cliente(idcliente) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: venda venda_idveiculo_id_9c435c4f_fk_veiculo_idveiculo; Type: FK CONSTRAINT; Schema: public; Owner: concessionaria
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT venda_idveiculo_id_9c435c4f_fk_veiculo_idveiculo FOREIGN KEY (idveiculo_id) REFERENCES public.veiculo(idveiculo) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

