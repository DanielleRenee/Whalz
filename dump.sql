--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: beers; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE beers (
    beer_code character varying(10) NOT NULL,
    name character varying(100) NOT NULL,
    style_id integer,
    year integer,
    abv double precision,
    beer_variation character varying(100),
    beer_variation_id character varying(100),
    ibu double precision
);


ALTER TABLE beers OWNER TO vagrant;

--
-- Name: inventories; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE inventories (
    inventory_id integer NOT NULL,
    beer_code character varying(10),
    user_id integer,
    quantity integer
);


ALTER TABLE inventories OWNER TO vagrant;

--
-- Name: inventories_inventory_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE inventories_inventory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE inventories_inventory_id_seq OWNER TO vagrant;

--
-- Name: inventories_inventory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE inventories_inventory_id_seq OWNED BY inventories.inventory_id;


--
-- Name: iso; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE iso (
    iso_id integer NOT NULL,
    beer_code character varying(10),
    user_id integer,
    quantity integer,
    active boolean NOT NULL
);


ALTER TABLE iso OWNER TO vagrant;

--
-- Name: iso_iso_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE iso_iso_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE iso_iso_id_seq OWNER TO vagrant;

--
-- Name: iso_iso_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE iso_iso_id_seq OWNED BY iso.iso_id;


--
-- Name: possible_trades; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE possible_trades (
    possible_id integer NOT NULL,
    inventory_id integer,
    iso_id integer
);


ALTER TABLE possible_trades OWNER TO vagrant;

--
-- Name: possible_trades_possible_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE possible_trades_possible_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE possible_trades_possible_id_seq OWNER TO vagrant;

--
-- Name: possible_trades_possible_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE possible_trades_possible_id_seq OWNED BY possible_trades.possible_id;


--
-- Name: trades; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE trades (
    trade_id integer NOT NULL,
    traded_at timestamp without time zone,
    quantity integer NOT NULL,
    initial_trade integer,
    reciprocal_trade integer
);


ALTER TABLE trades OWNER TO vagrant;

--
-- Name: trades_trade_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE trades_trade_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE trades_trade_id_seq OWNER TO vagrant;

--
-- Name: trades_trade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE trades_trade_id_seq OWNED BY trades.trade_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE users (
    user_id integer NOT NULL,
    name character varying(64) NOT NULL,
    email character varying(64) NOT NULL,
    password character varying(64) NOT NULL
);


ALTER TABLE users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- Name: inventory_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY inventories ALTER COLUMN inventory_id SET DEFAULT nextval('inventories_inventory_id_seq'::regclass);


--
-- Name: iso_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY iso ALTER COLUMN iso_id SET DEFAULT nextval('iso_iso_id_seq'::regclass);


--
-- Name: possible_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY possible_trades ALTER COLUMN possible_id SET DEFAULT nextval('possible_trades_possible_id_seq'::regclass);


--
-- Name: trade_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trades ALTER COLUMN trade_id SET DEFAULT nextval('trades_trade_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- Data for Name: beers; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY beers (beer_code, name, style_id, year, abv, beer_variation, beer_variation_id, ibu) FROM stdin;
4Vmwih	1912	32	\N	7	\N	\N	50
oQR5YM	1916 Irish Stout	42	\N	\N	\N	\N	\N
Qg6dpg	1916 Irish Stout	42	\N	3.5	\N	\N	\N
9wNKio	1916 Shore Shiver	30	\N	6.90000000000000036	\N	\N	\N
0DVz81	1919 Root Beer	139	\N	\N	\N	\N	\N
YP4dCI	1920 Cognac Stout Imperiale	132	\N	11.6400000000000006	\N	\N	82
Eyr9Kg	1926	25	\N	5	\N	\N	45
jT5vQ0	1927	29	\N	7.5	\N	\N	\N
6gWXP4	1938 Special	37	\N	5.70000000000000018	\N	\N	23
22sc9o	1945	46	\N	\N	\N	\N	\N
wAqRB6	1955 Double Brown	37	\N	5.09999999999999964	\N	\N	\N
Z7Sldi	1956 Golden Ale	36	\N	4.5	\N	\N	12
UbL8wu	1957 All Star Ale	10	\N	4	\N	\N	17
IiW61L	1972	14	\N	\N	\N	\N	\N
uqJO5U	199 Full Moon 16th Anniversary IllunaRator	90	\N	9.30000000000000071	\N	\N	\N
9hrCi9	1997	\N	\N	6.79999999999999982	\N	\N	\N
Z975kH	19th Amendment Imperial Stout	43	\N	7.79999999999999982	\N	\N	35
Bt3ISc	19th Anniversary Ale	31	\N	9	\N	\N	80
W9GM4Y	19th Anniversary Ale	104	\N	7.70000000000000018	\N	\N	30
BrAip0	19th Anniversary Ale	29	\N	10.1999999999999993	\N	\N	\N
4xP8AV	19th Anniversary Barleywine Style Imperial Stout	43	\N	10	\N	\N	43
KYmRUi	19th Birthday Suit	119	\N	7.29999999999999982	\N	\N	\N
TTFy4W	1PA	30	\N	6.79999999999999982	\N	\N	\N
Vi6fgq	1st Amendment Lager	93	\N	\N	\N	\N	\N
EXx0Ad	1st Amendment Lager	97	\N	4	\N	\N	\N
kQ42vv	1st Anniversary	98	\N	7.40000000000000036	\N	\N	61
lr3HfC	1st Anniversary Ale	31	\N	9.30000000000000071	\N	\N	100
MnNbtN	1st Anniversary Ale	114	\N	9	\N	\N	37
EwzrNg	1st Anniversary Ale	125	\N	7.59999999999999964	\N	\N	\N
b06lC1	1st Anniversary Black Lager	103	\N	8	\N	\N	35
y16meT	1st Anniversary Breakers Ball	72	\N	10.9000000000000004	\N	\N	\N
o9hhvy	1st Avenue River	25	\N	6	\N	\N	31
tvXEUg	1st Conversation	72	\N	5.5	\N	\N	29
UAOQPd	1st Cutting IPA	30	\N	7	\N	\N	70
H6Go7J	1st Edition: Cascade	164	\N	4.09999999999999964	\N	\N	\N
t4XVri	1st Gear IPA	30	\N	6.20000000000000018	\N	\N	68
AIoIJs	1st Noel (2003)	14	2003	4.79999999999999982	\N	\N	\N
myCAim	1st Street Ale	36	\N	5	\N	\N	14
AqrNij	1Up IPA	25	\N	7.5	\N	\N	65
uV2xqH	1ZENUFF	31	\N	11	\N	\N	100
7D0RRo	2	41	\N	7.5	\N	\N	\N
aXCKGg	2 AM Bike Ride	42	\N	4.59999999999999964	\N	\N	\N
CxBdtx	2 Anniversary Ale	64	\N	9	\N	\N	\N
MdaCfM	2 Biggie	34	\N	7.09999999999999964	\N	\N	\N
dyydfi	2 Bit	30	\N	\N	\N	\N	\N
96spPo	2 Brothers	25	\N	\N	\N	\N	\N
HCUkDv	2 Brothers Session IPA	164	\N	4.70000000000000018	\N	\N	61
U405po	2 Cilindri	18	\N	5	\N	\N	\N
O9Yz5Y	2 HOP PALE – CENTENNIAL / APOLLO	25	\N	5.79999999999999982	\N	\N	40
\.


--
-- Data for Name: inventories; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY inventories (inventory_id, beer_code, user_id, quantity) FROM stdin;
1	9wNKio	13	7
2	jT5vQ0	100	7
3	oQR5YM	2	7
4	0DVz81	78	7
5	kQ42vv	57	7
6	0DVz81	2	7
7	0DVz81	44	7
8	0DVz81	74	7
9	Qg6dpg	40	7
10	Qg6dpg	58	7
11	jT5vQ0	39	7
12	kQ42vv	72	7
13	0DVz81	6	7
14	oQR5YM	55	7
15	9wNKio	38	7
16	Eyr9Kg	94	7
17	Qg6dpg	49	7
18	9wNKio	99	7
19	YP4dCI	91	7
20	4Vmwih	76	7
\.


--
-- Name: inventories_inventory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('inventories_inventory_id_seq', 20, true);


--
-- Data for Name: iso; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY iso (iso_id, beer_code, user_id, quantity, active) FROM stdin;
1	9wNKio	29	1	t
2	Qg6dpg	32	1	t
3	0DVz81	25	1	t
4	jT5vQ0	57	1	t
5	Eyr9Kg	87	1	t
6	Eyr9Kg	64	1	t
7	oQR5YM	87	1	t
8	4Vmwih	91	1	t
9	YP4dCI	10	1	t
10	jT5vQ0	64	1	t
11	jT5vQ0	93	1	t
12	Eyr9Kg	57	1	t
13	kQ42vv	26	1	t
14	Qg6dpg	17	1	t
15	Qg6dpg	54	1	t
17	jT5vQ0	3	1	t
18	9wNKio	6	1	t
19	Qg6dpg	27	1	t
20	9wNKio	41	1	t
16	0DVz81	13	1	f
\.


--
-- Name: iso_iso_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('iso_iso_id_seq', 20, true);


--
-- Data for Name: possible_trades; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY possible_trades (possible_id, inventory_id, iso_id) FROM stdin;
1	13	16
2	8	16
3	7	16
4	6	16
5	4	16
6	13	3
7	8	3
8	7	3
9	6	3
10	4	3
11	20	8
12	18	20
13	15	20
14	1	20
15	18	18
16	15	18
17	1	18
18	18	1
19	15	1
20	1	1
21	16	12
22	16	6
23	16	5
24	11	17
25	2	17
26	11	11
27	2	11
28	11	10
29	2	10
30	11	4
31	2	4
32	12	13
33	5	13
34	14	7
35	3	7
36	17	19
37	10	19
38	9	19
39	17	15
40	10	15
41	9	15
42	17	14
43	10	14
44	9	14
45	17	2
46	10	2
47	9	2
48	19	9
\.


--
-- Name: possible_trades_possible_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('possible_trades_possible_id_seq', 48, true);


--
-- Data for Name: trades; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY trades (trade_id, traded_at, quantity, initial_trade, reciprocal_trade) FROM stdin;
1	2017-07-04 01:41:39.614057	1	4	22
2	2017-07-04 01:49:53.372789	1	19	9
3	2017-07-04 01:50:19.349085	1	7	3
4	2017-07-04 01:51:08.327493	1	10	2
5	2017-07-04 01:52:16.94981	1	1	18
6	2017-07-04 01:53:01.74184	1	17	2
\.


--
-- Name: trades_trade_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('trades_trade_id_seq', 6, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY users (user_id, name, email, password) FROM stdin;
1	Robert Sims	taylorjames@yahoo.com	R!4wMY_Vct
2	Alexis Fitzpatrick MD	darryllyons@green.net	@^Xmo5v414
3	Robert Brewer	pbrown@douglas-holmes.com	n5PQa9#e*K
4	Isabel Anderson	evansrebecca@young.com	R#1MkpK&^b
5	Emily Price	alexandria54@stephens-wilson.info	cNs!71Hxly
6	Laura Ford	brian26@yahoo.com	5yN&Z3t&#S
7	Lauren Ramirez	taylorkimberly@gmail.com	i2G65_kd^h
8	Adrian Gonzalez	jdickson@lewis.com	fcLDpU*1_6
9	Dawn Smith	westjohn@rivera.org	sV6X5WsvS)
10	Robert Banks	qpatton@hotmail.com	q(lXyYHwk9
11	Clinton Pierce	hillsharon@hotmail.com	K!k6MV+y*+
12	Valerie Tapia	christinerivera@mcdaniel.org	pVq4+Zogw+
13	Brent Chavez	dhouston@gibson-allen.com	)!3dMkmRKV
14	Steven Valencia	nina62@walsh.com	Zo!4MorNn&
15	Sarah Carter	wongnicole@cooke-jackson.com	(VxoVsYw$7
16	Kelly Fuller	dperez@porter.org	Ddw9bbMY+@
17	Jennifer Lewis	mhorton@hendricks.org	*KBoZRRs7B
18	John Reilly	sarah10@jenkins.com	b@S5FyMg#C
19	Dr. Jennifer Wilson	craig25@gmail.com	#&2xWalcwJ
20	Destiny Oconnor	paul64@powers.com	%2SD(s2zi5
21	Kathy Cummings	muellerkevin@le.com	A20NfoQue_
22	Nathan Gray	christopher71@gmail.com	CDAnvjh0!4
23	Elizabeth Thomas	owright@hotmail.com	8DwWAeQ!_P
24	Samantha White	brandi07@yahoo.com	a1^6XAso+*
25	Robert Dean	clementsvickie@gmail.com	#h0OmObU%3
26	Ryan Dominguez	huangrandy@martinez-smith.com	y+^dw1PxNm
27	Elizabeth Hudson	davidibarra@buckley.org	LPNsPZr7!0
28	Erin Johnson	claudia99@hotmail.com	fM!@6SFjJW
29	Richard Ali	frangel@whitaker.org	D$60HLn1C!
30	Philip Peterson	jennifer11@gmail.com	0DSmNgga)a
31	Kevin Morales	ubrady@ross.com	Oy8S6MqZC%
32	Jeremy Solomon	hatfieldnicole@hall.com	ae0Qtm$u**
33	Joseph Mcgee	megan46@gmail.com	%0qPGrumgu
34	Amber Diaz	robert96@hotmail.com	&R8B&vBe$(
35	Miguel Long	iconner@yahoo.com	%S#Zg5m@35
36	Michael Collins	ronald28@graham-mcdonald.net	#_41lQhsh_
37	Tammy Cuevas	gina87@anderson-carter.com	^hU2J2L(%&
38	Michael Lawson	rbrooks@fisher-bolton.net	Qq7SQdcY@b
39	Jessica Scott	michellemiller@francis-lee.info	reSkEL1r&1
40	Heather Burton	rileymatthew@gmail.com	XG3ZAfpsT#
41	Elizabeth Holmes	gkrause@yahoo.com	&6WzZTF8w6
42	Jacob Baker	fergusondeborah@gmail.com	*omEGGV^e7
43	Garrett Moreno	kiddmariah@gmail.com	&d7Qptqsq3
44	Joshua Lynch	fisherbrittany@nelson.com	+!Q&kJQxP8
45	Andrew Ford	kaufmannicholas@gmail.com	I%rX9F33br
46	Francisco Garcia	kellyjustin@marsh.net	GO7*Jwen$(
47	Elizabeth Brown	parkerlisa@collins-castro.com	TQmO_M$b+7
48	Kimberly Gordon	morgangomez@wheeler.info	rlO_8LgqJH
49	Erin Velasquez	gonzaleseric@watkins.org	G3YD6c&#!b
50	Claire Cruz	kristakelly@phillips-valencia.org	n*D@5GAjKc
51	Michael Brown	gmahoney@perez.com	v8JiX&US%C
52	Jacob Le	robertwright@yahoo.com	+)sOfyK38W
53	Benjamin Klein	welliott@williams-cline.biz	TPQfkAp_#7
54	Susan Perez	baldwinchristopher@smith.com	(J(4Es&o&7
55	Casey Farrell DVM	ygraham@davis-bennett.com	Jb#T7BgV2B
56	Ricardo Carter	edwardssherry@pearson.com	(3%VAttcM1
57	Thomas Johnson	caroline21@gmail.com	&suuQCLk13
58	Scott Norman	mary16@yahoo.com	w*8B)6PlaC
59	Erik Morales	rjoseph@calhoun.info	2!b&4dZo*&
60	Charles Jordan	andrew99@miller-ibarra.com	g9LfkfY0%j
61	Ronald Wheeler	cgrant@boone.biz	II0Sh3AaQ#
62	Aaron Smith	mbriggs@bates.org	T!!eV2Yk4R
63	Christopher Ochoa	richard47@hotmail.com	R5BGfkvr$Y
64	Nicholas Miranda	dixontimothy@simmons.net	mv1F0D1VP$
65	Gary Peterson	derrick85@hotmail.com	t)4TBMExkB
66	Stacy Colon	kristina08@lloyd.com	H)F8DEd4XD
67	Anna Walker	zpatton@yahoo.com	5vBpN)2g+4
68	Lori Sanchez	dpope@hotmail.com	(#7VItGmxo
69	Brooke Johnson	richardmendoza@miller.com	(#8r+RrqDD
70	Adam Green	christinamartinez@leach.com	N+y8Cv+pVZ
71	Mallory Bernard MD	efloyd@crawford.com	qK&k3YhkK4
72	Brandon Gonzales	cbowers@lee.com	N)5BLuFRLh
73	Joseph Santos	kingmatthew@acosta.com	+V&^^Lg&@1
74	Robert Humphrey	tonya76@yahoo.com	(QAq40pc42
75	Kerry Wood	manuel11@miller.org	DG2ZUbueW*
76	Samuel Barber	fhenry@gmail.com	0q4NCCYs%V
77	Jennifer Goodman	kristin42@fields.biz	$5L191or00
78	Anthony James	eduardomyers@gmail.com	0%2OQVmP6M
79	Kenneth Lynch	tammy51@roth.com	!y7qAUlIOc
80	Brent Green	claytonadkins@evans.com	6%N1%v)M&R
81	Thomas Green	reynoldsveronica@gmail.com	_^OLtxbDg1
82	Jennifer Hawkins	cfrye@carrillo.com	*t7ElAm5_j
83	Keith Ford	dannydelgado@gmail.com	915LxBjJ+%
84	Tiffany Flores	pcobb@higgins-wilson.org	wFPEfeqe$3
85	Jose Becker	darryl31@daniels.com	r4%7rNqE9K
86	Cathy Thomas	henry88@miller.biz	6_071OAaX7
87	Michael Hudson	lisamelton@gmail.com	&1#l^QdZNw
88	Melissa Wu	phillipsnicole@rubio.org	V!2g0ALlVD
89	Julie Simpson	wyattyesenia@yahoo.com	!z*(76ZiAc
90	Sarah Branch	pamelawelch@andrews.biz	qo2y3pCtF(
91	Ricky Rose	cunninghamjessica@hotmail.com	&oC6QCn%yU
92	Billy Floyd	donnaortiz@harper-figueroa.com	*_bOwoHy_9
93	Lori Ford	carterleah@gmail.com	A2%xLZo&%L
94	Patricia Park	joshuaruiz@hotmail.com	^ws24XxlK!
95	Misty Ray	hjones@carrillo.com	$2GWR_Fp^m
96	Angel Stevens	buckrandy@gmail.com	Q^7_7Nxw(B
97	Brian Johnson	moniquelittle@palmer.com	Te0K@aei(Z
98	Michael Hanson	abarker@hotmail.com	s)3B!$4n!G
99	Bethany Malone	ryanwarren@turner.com	B+5P5H3qEc
100	James Bishop	walterbarnett@yahoo.com	H_$8)sXym1
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('users_user_id_seq', 100, true);


--
-- Name: beers_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY beers
    ADD CONSTRAINT beers_pkey PRIMARY KEY (beer_code);


--
-- Name: inventories_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY inventories
    ADD CONSTRAINT inventories_pkey PRIMARY KEY (inventory_id);


--
-- Name: iso_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY iso
    ADD CONSTRAINT iso_pkey PRIMARY KEY (iso_id);


--
-- Name: possible_trades_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY possible_trades
    ADD CONSTRAINT possible_trades_pkey PRIMARY KEY (possible_id);


--
-- Name: trades_initial_trade_reciprocal_trade_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trades
    ADD CONSTRAINT trades_initial_trade_reciprocal_trade_key UNIQUE (initial_trade, reciprocal_trade);


--
-- Name: trades_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trades
    ADD CONSTRAINT trades_pkey PRIMARY KEY (trade_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: ix_inventories_beer_code; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_inventories_beer_code ON inventories USING btree (beer_code);


--
-- Name: ix_inventories_user_id; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_inventories_user_id ON inventories USING btree (user_id);


--
-- Name: ix_iso_beer_code; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_iso_beer_code ON iso USING btree (beer_code);


--
-- Name: ix_iso_user_id; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_iso_user_id ON iso USING btree (user_id);


--
-- Name: ix_possible_trades_inventory_id; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_possible_trades_inventory_id ON possible_trades USING btree (inventory_id);


--
-- Name: ix_possible_trades_iso_id; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_possible_trades_iso_id ON possible_trades USING btree (iso_id);


--
-- Name: ix_trades_initial_trade; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_trades_initial_trade ON trades USING btree (initial_trade);


--
-- Name: ix_trades_reciprocal_trade; Type: INDEX; Schema: public; Owner: vagrant
--

CREATE INDEX ix_trades_reciprocal_trade ON trades USING btree (reciprocal_trade);


--
-- Name: inventories_beer_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY inventories
    ADD CONSTRAINT inventories_beer_code_fkey FOREIGN KEY (beer_code) REFERENCES beers(beer_code);


--
-- Name: inventories_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY inventories
    ADD CONSTRAINT inventories_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: iso_beer_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY iso
    ADD CONSTRAINT iso_beer_code_fkey FOREIGN KEY (beer_code) REFERENCES beers(beer_code);


--
-- Name: iso_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY iso
    ADD CONSTRAINT iso_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: possible_trades_inventory_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY possible_trades
    ADD CONSTRAINT possible_trades_inventory_id_fkey FOREIGN KEY (inventory_id) REFERENCES inventories(inventory_id);


--
-- Name: possible_trades_iso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY possible_trades
    ADD CONSTRAINT possible_trades_iso_id_fkey FOREIGN KEY (iso_id) REFERENCES iso(iso_id);


--
-- Name: trades_initial_trade_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trades
    ADD CONSTRAINT trades_initial_trade_fkey FOREIGN KEY (initial_trade) REFERENCES possible_trades(possible_id);


--
-- Name: trades_reciprocal_trade_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trades
    ADD CONSTRAINT trades_reciprocal_trade_fkey FOREIGN KEY (reciprocal_trade) REFERENCES possible_trades(possible_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

