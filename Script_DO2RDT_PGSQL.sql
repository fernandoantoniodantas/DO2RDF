PGDMP          ,                x            diario     12.3 (Ubuntu 12.3-1.pgdg18.04+1)     12.3 (Ubuntu 12.3-1.pgdg18.04+1) #    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16384    diario    DATABASE     x   CREATE DATABASE diario WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'pt_BR.UTF-8' LC_CTYPE = 'pt_BR.UTF-8';
    DROP DATABASE diario;
                postgres    false            	            2615    16385    dorj    SCHEMA        CREATE SCHEMA dorj;
    DROP SCHEMA dorj;
                postgres    false            �            1259    16388    atos    TABLE     �   CREATE TABLE dorj.atos (
    id bigint NOT NULL,
    matricula text,
    nome text,
    datapublicacao date,
    dataefeito date,
    cargo text,
    tipocargo text,
    acao text,
    simbolo text,
    idpes bigint,
    idcargo bigint
);
    DROP TABLE dorj.atos;
       dorj         heap    postgres    false    9            �            1259    16386    atos_id_seq    SEQUENCE     r   CREATE SEQUENCE dorj.atos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
     DROP SEQUENCE dorj.atos_id_seq;
       dorj          postgres    false    9    205            �           0    0    atos_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE dorj.atos_id_seq OWNED BY dorj.atos.id;
          dorj          postgres    false    204            �            1259    49194    cargos    TABLE     j   CREATE TABLE dorj.cargos (
    id bigint NOT NULL,
    descricao text,
    tipo text,
    simbolo text
);
    DROP TABLE dorj.cargos;
       dorj         heap    postgres    false    9            �            1259    49192    cargos_id_seq    SEQUENCE     t   CREATE SEQUENCE dorj.cargos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE dorj.cargos_id_seq;
       dorj          postgres    false    217    9            �           0    0    cargos_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE dorj.cargos_id_seq OWNED BY dorj.cargos.id;
          dorj          postgres    false    216            �            1259    16409    diarios    TABLE     �   CREATE TABLE dorj.diarios (
    id bigint NOT NULL,
    numero integer,
    tipo integer,
    ano bigint,
    anoromano character(15),
    datadiario date,
    datagravacao date[],
    identidade bigint[],
    arquivo bytea[],
    nomearquivo text[]
);
    DROP TABLE dorj.diarios;
       dorj         heap    postgres    false    9            �            1259    16407    diarios_id_seq    SEQUENCE     u   CREATE SEQUENCE dorj.diarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE dorj.diarios_id_seq;
       dorj          postgres    false    207    9            �           0    0    diarios_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE dorj.diarios_id_seq OWNED BY dorj.diarios.id;
          dorj          postgres    false    206            �            1259    32799 	   entidades    TABLE     e   CREATE TABLE dorj.entidades (
    id bigint NOT NULL,
    descricao text[],
    idesfera bigint[]
);
    DROP TABLE dorj.entidades;
       dorj         heap    postgres    false    9            �            1259    32802    entidades_id_seq    SEQUENCE     w   CREATE SEQUENCE dorj.entidades_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE dorj.entidades_id_seq;
       dorj          postgres    false    212    9            �           0    0    entidades_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE dorj.entidades_id_seq OWNED BY dorj.entidades.id;
          dorj          postgres    false    213            �            1259    49185    pessoas    TABLE     E   CREATE TABLE dorj.pessoas (
    id bigint NOT NULL,
    nome text
);
    DROP TABLE dorj.pessoas;
       dorj         heap    postgres    false    9            �            1259    49183    pessoas_id_seq    SEQUENCE     u   CREATE SEQUENCE dorj.pessoas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE dorj.pessoas_id_seq;
       dorj          postgres    false    215    9            �           0    0    pessoas_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE dorj.pessoas_id_seq OWNED BY dorj.pessoas.id;
          dorj          postgres    false    214            #           2604    16391    atos id    DEFAULT     ^   ALTER TABLE ONLY dorj.atos ALTER COLUMN id SET DEFAULT nextval('dorj.atos_id_seq'::regclass);
 4   ALTER TABLE dorj.atos ALTER COLUMN id DROP DEFAULT;
       dorj          postgres    false    204    205    205            '           2604    49197 	   cargos id    DEFAULT     b   ALTER TABLE ONLY dorj.cargos ALTER COLUMN id SET DEFAULT nextval('dorj.cargos_id_seq'::regclass);
 6   ALTER TABLE dorj.cargos ALTER COLUMN id DROP DEFAULT;
       dorj          postgres    false    216    217    217            $           2604    16412 
   diarios id    DEFAULT     d   ALTER TABLE ONLY dorj.diarios ALTER COLUMN id SET DEFAULT nextval('dorj.diarios_id_seq'::regclass);
 7   ALTER TABLE dorj.diarios ALTER COLUMN id DROP DEFAULT;
       dorj          postgres    false    206    207    207            %           2604    32804    entidades id    DEFAULT     h   ALTER TABLE ONLY dorj.entidades ALTER COLUMN id SET DEFAULT nextval('dorj.entidades_id_seq'::regclass);
 9   ALTER TABLE dorj.entidades ALTER COLUMN id DROP DEFAULT;
       dorj          postgres    false    213    212            &           2604    49188 
   pessoas id    DEFAULT     d   ALTER TABLE ONLY dorj.pessoas ALTER COLUMN id SET DEFAULT nextval('dorj.pessoas_id_seq'::regclass);
 7   ALTER TABLE dorj.pessoas ALTER COLUMN id DROP DEFAULT;
       dorj          postgres    false    214    215    215            �          0    16388    atos 
   TABLE DATA           ~   COPY dorj.atos (id, matricula, nome, datapublicacao, dataefeito, cargo, tipocargo, acao, simbolo, idpes, idcargo) FROM stdin;
    dorj          postgres    false    205   Z"       �          0    49194    cargos 
   TABLE DATA           <   COPY dorj.cargos (id, descricao, tipo, simbolo) FROM stdin;
    dorj          postgres    false    217   w"       �          0    16409    diarios 
   TABLE DATA           }   COPY dorj.diarios (id, numero, tipo, ano, anoromano, datadiario, datagravacao, identidade, arquivo, nomearquivo) FROM stdin;
    dorj          postgres    false    207   �"       �          0    32799 	   entidades 
   TABLE DATA           :   COPY dorj.entidades (id, descricao, idesfera) FROM stdin;
    dorj          postgres    false    212   �"       �          0    49185    pessoas 
   TABLE DATA           )   COPY dorj.pessoas (id, nome) FROM stdin;
    dorj          postgres    false    215   �"       �           0    0    atos_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('dorj.atos_id_seq', 25197, true);
          dorj          postgres    false    204            �           0    0    cargos_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('dorj.cargos_id_seq', 434, true);
          dorj          postgres    false    216            �           0    0    diarios_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('dorj.diarios_id_seq', 628, true);
          dorj          postgres    false    206            �           0    0    entidades_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('dorj.entidades_id_seq', 1, false);
          dorj          postgres    false    213            �           0    0    pessoas_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('dorj.pessoas_id_seq', 9440, true);
          dorj          postgres    false    214            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     