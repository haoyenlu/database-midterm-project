PGDMP     *    &            
    y            new_surf    13.4    13.4 $    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    17020    new_surf    DATABASE     r   CREATE DATABASE new_surf WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Chinese (Traditional)_Taiwan.950';
    DROP DATABASE new_surf;
                postgres    false                        2615    17021    SURF    SCHEMA        CREATE SCHEMA "SURF";
    DROP SCHEMA "SURF";
                postgres    false            ?            1259    17022    INFORMATION    TABLE     &  CREATE TABLE "SURF"."INFORMATION" (
    "Spot_id" integer NOT NULL,
    "Date" text NOT NULL,
    "Wave_height" real,
    "Wave_period" real,
    "Wave_direction" real,
    "Wind_speed" real,
    "Wind_direction" real,
    "Temperature" real,
    "Sea_temperature" real,
    "Score" integer
);
 !   DROP TABLE "SURF"."INFORMATION";
       SURF         heap    postgres    false    6            ?            1259    17028    NEWS    TABLE     ?   CREATE TABLE "SURF"."NEWS" (
    "Id" integer NOT NULL,
    "Date" text,
    "Url" text,
    "Title" text,
    "Spot_id" integer
);
    DROP TABLE "SURF"."NEWS";
       SURF         heap    postgres    false    6            ?            1259    17034 	   RECOMMEND    TABLE     ?   CREATE TABLE "SURF"."RECOMMEND" (
    "Reviewer_id" integer NOT NULL,
    "Spot_id" integer NOT NULL,
    "Score" integer,
    "Content" text,
    "Date" text
);
    DROP TABLE "SURF"."RECOMMEND";
       SURF         heap    postgres    false    6            ?            1259    17040    REVIEWER    TABLE     a   CREATE TABLE "SURF"."REVIEWER" (
    "Id" integer NOT NULL,
    "Name" text,
    "Email" text
);
    DROP TABLE "SURF"."REVIEWER";
       SURF         heap    postgres    false    6            ?            1259    17046    SPOT    TABLE     ?   CREATE TABLE "SURF"."SPOT" (
    "Id" integer NOT NULL,
    "Name" text,
    "Lon" real,
    "Lat" real,
    "Town_id" character(3),
    "Type_id" integer
);
    DROP TABLE "SURF"."SPOT";
       SURF         heap    postgres    false    6            ?            1259    17052    SURFSHOP    TABLE     ?   CREATE TABLE "SURF"."SURFSHOP" (
    "Id" integer NOT NULL,
    "Name" text,
    "Address" text,
    "Spot_id" integer,
    "Rating" real,
    "Operating_now" boolean
);
    DROP TABLE "SURF"."SURFSHOP";
       SURF         heap    postgres    false    6            ?            1259    17058    TOWN    TABLE     a   CREATE TABLE "SURF"."TOWN" (
    "Id" character(3) NOT NULL,
    "Name" text,
    "City" text
);
    DROP TABLE "SURF"."TOWN";
       SURF         heap    postgres    false    6            ?            1259    17064    TYPE    TABLE     T   CREATE TABLE "SURF"."TYPE" (
    "Id" integer NOT NULL,
    "Name" text NOT NULL
);
    DROP TABLE "SURF"."TYPE";
       SURF         heap    postgres    false    6            ?          0    17022    INFORMATION 
   TABLE DATA           ?   COPY "SURF"."INFORMATION" ("Spot_id", "Date", "Wave_height", "Wave_period", "Wave_direction", "Wind_speed", "Wind_direction", "Temperature", "Sea_temperature", "Score") FROM stdin;
    SURF          postgres    false    201   (       ?          0    17028    NEWS 
   TABLE DATA           I   COPY "SURF"."NEWS" ("Id", "Date", "Url", "Title", "Spot_id") FROM stdin;
    SURF          postgres    false    202   *(       ?          0    17034 	   RECOMMEND 
   TABLE DATA           [   COPY "SURF"."RECOMMEND" ("Reviewer_id", "Spot_id", "Score", "Content", "Date") FROM stdin;
    SURF          postgres    false    203   G(       ?          0    17040    REVIEWER 
   TABLE DATA           ;   COPY "SURF"."REVIEWER" ("Id", "Name", "Email") FROM stdin;
    SURF          postgres    false    204   d(       ?          0    17046    SPOT 
   TABLE DATA           R   COPY "SURF"."SPOT" ("Id", "Name", "Lon", "Lat", "Town_id", "Type_id") FROM stdin;
    SURF          postgres    false    205   ?(       ?          0    17052    SURFSHOP 
   TABLE DATA           c   COPY "SURF"."SURFSHOP" ("Id", "Name", "Address", "Spot_id", "Rating", "Operating_now") FROM stdin;
    SURF          postgres    false    206   ?(       ?          0    17058    TOWN 
   TABLE DATA           6   COPY "SURF"."TOWN" ("Id", "Name", "City") FROM stdin;
    SURF          postgres    false    207   ?(       ?          0    17064    TYPE 
   TABLE DATA           .   COPY "SURF"."TYPE" ("Id", "Name") FROM stdin;
    SURF          postgres    false    208   ?(       F           2606    17072    INFORMATION INFORMATION_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY "SURF"."INFORMATION"
    ADD CONSTRAINT "INFORMATION_pkey" PRIMARY KEY ("Spot_id", "Date");
 J   ALTER TABLE ONLY "SURF"."INFORMATION" DROP CONSTRAINT "INFORMATION_pkey";
       SURF            postgres    false    201    201            H           2606    17074    NEWS NEWS_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY "SURF"."NEWS"
    ADD CONSTRAINT "NEWS_pkey" PRIMARY KEY ("Id");
 <   ALTER TABLE ONLY "SURF"."NEWS" DROP CONSTRAINT "NEWS_pkey";
       SURF            postgres    false    202            L           2606    17076    REVIEWER REVIEWER_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY "SURF"."REVIEWER"
    ADD CONSTRAINT "REVIEWER_pkey" PRIMARY KEY ("Id");
 D   ALTER TABLE ONLY "SURF"."REVIEWER" DROP CONSTRAINT "REVIEWER_pkey";
       SURF            postgres    false    204            J           2606    17078    RECOMMEND Recommend_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY "SURF"."RECOMMEND"
    ADD CONSTRAINT "Recommend_pkey" PRIMARY KEY ("Reviewer_id", "Spot_id");
 F   ALTER TABLE ONLY "SURF"."RECOMMEND" DROP CONSTRAINT "Recommend_pkey";
       SURF            postgres    false    203    203            N           2606    17080    SPOT SPOT_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY "SURF"."SPOT"
    ADD CONSTRAINT "SPOT_pkey" PRIMARY KEY ("Id");
 <   ALTER TABLE ONLY "SURF"."SPOT" DROP CONSTRAINT "SPOT_pkey";
       SURF            postgres    false    205            P           2606    17082    SURFSHOP SURFSHOP_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY "SURF"."SURFSHOP"
    ADD CONSTRAINT "SURFSHOP_pkey" PRIMARY KEY ("Id");
 D   ALTER TABLE ONLY "SURF"."SURFSHOP" DROP CONSTRAINT "SURFSHOP_pkey";
       SURF            postgres    false    206            R           2606    17084    TOWN TOWN_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY "SURF"."TOWN"
    ADD CONSTRAINT "TOWN_pkey" PRIMARY KEY ("Id");
 <   ALTER TABLE ONLY "SURF"."TOWN" DROP CONSTRAINT "TOWN_pkey";
       SURF            postgres    false    207            T           2606    17086    TYPE TYPE_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY "SURF"."TYPE"
    ADD CONSTRAINT "TYPE_pkey" PRIMARY KEY ("Id");
 <   ALTER TABLE ONLY "SURF"."TYPE" DROP CONSTRAINT "TYPE_pkey";
       SURF            postgres    false    208            W           2606    17087    RECOMMEND FK_Reviewer    FK CONSTRAINT     ?   ALTER TABLE ONLY "SURF"."RECOMMEND"
    ADD CONSTRAINT "FK_Reviewer" FOREIGN KEY ("Reviewer_id") REFERENCES "SURF"."REVIEWER"("Id");
 C   ALTER TABLE ONLY "SURF"."RECOMMEND" DROP CONSTRAINT "FK_Reviewer";
       SURF          postgres    false    2892    203    204            [           2606    17092    SURFSHOP FK_Spot    FK CONSTRAINT     ?   ALTER TABLE ONLY "SURF"."SURFSHOP"
    ADD CONSTRAINT "FK_Spot" FOREIGN KEY ("Spot_id") REFERENCES "SURF"."SPOT"("Id") NOT VALID;
 >   ALTER TABLE ONLY "SURF"."SURFSHOP" DROP CONSTRAINT "FK_Spot";
       SURF          postgres    false    205    206    2894            V           2606    17097    NEWS FK_Spot    FK CONSTRAINT     t   ALTER TABLE ONLY "SURF"."NEWS"
    ADD CONSTRAINT "FK_Spot" FOREIGN KEY ("Spot_id") REFERENCES "SURF"."SPOT"("Id");
 :   ALTER TABLE ONLY "SURF"."NEWS" DROP CONSTRAINT "FK_Spot";
       SURF          postgres    false    205    202    2894            U           2606    17102    INFORMATION FK_Spot    FK CONSTRAINT     ?   ALTER TABLE ONLY "SURF"."INFORMATION"
    ADD CONSTRAINT "FK_Spot" FOREIGN KEY ("Spot_id") REFERENCES "SURF"."SPOT"("Id") NOT VALID;
 A   ALTER TABLE ONLY "SURF"."INFORMATION" DROP CONSTRAINT "FK_Spot";
       SURF          postgres    false    205    201    2894            X           2606    17107    RECOMMEND FK_Spot    FK CONSTRAINT     y   ALTER TABLE ONLY "SURF"."RECOMMEND"
    ADD CONSTRAINT "FK_Spot" FOREIGN KEY ("Spot_id") REFERENCES "SURF"."SPOT"("Id");
 ?   ALTER TABLE ONLY "SURF"."RECOMMEND" DROP CONSTRAINT "FK_Spot";
       SURF          postgres    false    203    205    2894            Y           2606    17112    SPOT FK_Town    FK CONSTRAINT     ~   ALTER TABLE ONLY "SURF"."SPOT"
    ADD CONSTRAINT "FK_Town" FOREIGN KEY ("Town_id") REFERENCES "SURF"."TOWN"("Id") NOT VALID;
 :   ALTER TABLE ONLY "SURF"."SPOT" DROP CONSTRAINT "FK_Town";
       SURF          postgres    false    205    2898    207            Z           2606    17117    SPOT FK_Type    FK CONSTRAINT     ~   ALTER TABLE ONLY "SURF"."SPOT"
    ADD CONSTRAINT "FK_Type" FOREIGN KEY ("Type_id") REFERENCES "SURF"."TYPE"("Id") NOT VALID;
 :   ALTER TABLE ONLY "SURF"."SPOT" DROP CONSTRAINT "FK_Type";
       SURF          postgres    false    2900    205    208            ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?     