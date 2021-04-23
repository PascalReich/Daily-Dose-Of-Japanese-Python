#Libraries
import tkinter
from tkinter import ttk
import openpyxl
import pandas as pd
import pyperclip
import datetime
import webbrowser
import kanji

#Kanjis Lists
HeisigEs = {"晶" : "destello", "七": "siete", "朋": "compañera", "古": "viejo", "月": "mes", "九": "nueve", "八": "ocho", "吾": "yo", "二": "dos", "昌": "prospero", "早": "temprano", "五": "cinco", "一": "uno", "六": "seis", "田": "campo de arroz", "冒": "riesgo", "口": "boca", "十": "diez", "呂": "espina dorsal", "明": "claro", "三": "tres", "品": "mercancias", "目": "ojo", "唱": "canto", "旭": "sol naciente", "世": "generacion", "四": "cuatro", "日": "dia", "占": "adivinacion", "亘": "atravesar", "下": "abajo", "升": "caja para medir", "千": "mil", "貝": "almeja", "朝": "mañana", "博": "Dr.", "自": "uno mismo", "胃": "estomago", "寸": "medida", "専": "especialidad", "胆": "vesicula biliar", "百": "cien", "昇": "elevarse", "只": "unico", "凸": "convexo", "舌": "lengua", "凹": "concavo", "丸": "redondo", "旧": "antigüedad", "中": "en", "旦": "amanecer", "貞": "recto", "白": "blanco", "卓": "eminente", "上": "arriba", "見": "ver", "旬": "decameron", "勺": "cucharon", "的": "diana", "直": "directamente", "乙": "entrañas de pescado", "左": "izquierda", "乱": "tumulto", "員": "empleado", "凡": "mediocre", "肌": "piel", "真": "verdad", "元": "principio", "負": "derrota", "項": "parrafo", "賄": "soborno", "貢": "tributo", "有": "posesion", "工": "tecnica", "具": "herramienta", "首": "cuello", "万": "diez mil", "頑": "tozudo", "句": "frase", "児": "recien nacido", "頁": "pagina", "右": "derecha", "刀": "espada", "多": "muchos", "母": "madre", "如": "parecido", "大": "grande", "可": "posible", "別": "separar", "外": "exterior", "刃": "filo", "子": "niño", "町": "barrio", "夕": "noche", "克": "superar", "召": "seducir", "丁": "calle", "女": "mujer", "了": "acabado", "切": "cortar", "頂": "cima", "汐": "marea nocturna", "則": "norma", "副": "vice-", "貫": "traspasar", "好": "gustar", "少": "poco", "孔": "Confucio", "兄": "hermano mayor", "小": "pequeño", "昭": "brillante", "砂": "arena", "厚": "grueso", "器": "utensilio", "硝": "nitrato", "肖": "semejanza", "光": "rayo", "順": "obedecer", "沼": "pantano", "原": "prado", "臭": "apestar", "氷": "hielo", "太": "gordo", "省": "reflexionar", "願": "peticion", "泉": "manantial", "永": "eternidad", "水": "agua", "州": "estado", "石": "piedra", "名": "nombre", "削": "cepillar", "沖": "alta mar", "奇": "extraño", "川": "arroyo", "妙": "exquisita", "砕": "aplastar", "泳": "nadar", "活": "animado", "埼": "cabo", "潮": "marea", "畑": "plantacion", "圭": "joya cuadrada", "況": "por supuesto", "消": "extinguir", "測": "sondear", "灯": "lampara", "涯": "horizonte", "汁": "sopa", "河": "rio", "土": "tierra", "均": "anivelado", "江": "riachuelo", "泊": "pernoctar", "炎": "inflamacion", "淡": "diluido", "寺": "templo budista", "吐": "escupir", "時": "tiempo", "湖": "lago", "煩": "angustia", "垣": "valla", "火": "fuego", "源": "origen", "圧": "presion", "封": "sellar", "尚": "estimado", "照": "iluminar", "胴": "tronco", "安": "relajo", "墨": "tinta china", "洞": "cueva", "厘": "rin", "里": "ri", "埋": "enterrar", "宴": "banquete", "漁": "pescar", "宣": "proclamar", "守": "proteger", "字": "letra", "量": "cantidad", "完": "perfecto", "同": "el mismo", "点": "punto", "宵": "anochecer", "鯉": "carpa", "魚": "pescado", "黒": "negro", "向": "en frente de", "灰": "ceniza", "富": "riqueza", "寄": "acercarse", "災": "desastre", "味": "sabor", "桂": "katsura", "桐": "paulonia", "暦": "calendario", "柏": "roble", "末": "extremo", "相": "inter-", "枠": "marco", "村": "pueblo", "妹": "hermana menor", "木": "arbol", "貯": "ahorros", "枯": "marchitado", "杏": "albaricoque", "札": "etiqueta", "朴": "bruto", "森": "bosque", "机": "escritorio", "未": "todavia", "植": "plantar", "棚": "estanteria", "林": "arboleda", "案": "plan", "燥": "agostar", "沫": "salpicadura", "朱": "carmesi", "梢": "copa del arbol", "本": "libro", "株": "acciones de bolsa", "荻": "caña", "葉": "hoja", "苗": "planton", "模": "imitacion", "薄": "desteñido", "暮": "ganarse la vida", "黙": "silencio", "眺": "mirar fijamente", "状": "statu quo", "兆": "augurio", "寛": "tolerancia", "特": "especial", "先": "antes", "狩": "cazar", "漠": "borroso", "告": "revelacion", "然": "tal como es", "猫": "gato", "膜": "membrana", "洗": "lavar", "牛": "vaca", "桃": "melocoton", "犬": "perro", "若": "juventud", "苦": "sufrimiento", "墓": "tumba", "草": "hierba", "呈": "ofrenda", "茶": "te", "道": "camino", "界": "mundo", "全": "todo", "鉢": "bol", "金": "oro", "鎮": "tranquilizar", "柱": "columna", "理": "logica", "銅": "cobre", "狂": "loco", "介": "apretado", "皇": "emperador", "銘": "inscripcion", "合": "encajar", "注": "verter", "針": "aguja", "塔": "pagoda", "王": "rey", "現": "presente", "珠": "perla", "宝": "tesoro", "主": "amo", "玉": "joya", "釣": "pescar con caña", "導": "guiar", "栓": "tapon", "銑": "lingote", "落": "caer", "迫": "apremiar", "輝": "radiante", "連": "acompañar", "高": "alto", "夏": "verano", "逃": "escapar", "輸": "transportar", "巡": "patrullar", "造": "crear", "客": "invitado", "軍": "ejercito", "処": "deshacerse de", "冠": "corona", "略": "abreviatura", "享": "recibir", "軌": "carril", "格": "categoria", "夢": "sueño", "坑": "foso", "迅": "veloz", "辻": "cruce", "辺": "inmediaciones", "条": "ramita", "前": "delante", "冗": "superfluo", "各": "cada uno", "額": "frente", "運": "llevar", "車": "carruaje", "警": "amonestar", "週": "semana", "景": "paisaje", "敗": "fracaso", "敬": "respeto", "津": "ensenada", "舎": "casa de campo", "京": "capital", "覚": "memorizar", "故": "casualidad", "栄": "florecer", "周": "circunferencia", "壮": "robusto", "牧": "criar", "枚": "hojas de", "売": "venta", "吉": "buena suerte", "獄": "carcel", "言": "decir", "鯨": "ballena", "学": "estudiar", "熟": "madurar", "士": "hidalgo", "塾": "academia de repaso", "攻": "agresion", "訂": "revision", "計": "proyecto", "荘": "chalet", "涼": "refrescante", "亭": "pabellon", "書": "escribir", "語": "palabra", "滅": "destruir", "詰": "atascado", "談": "discusion", "成": "convertirse", "読": "leer", "諭": "reproche", "賊": "bandido", "詔": "edicto imperial", "浅": "poco profundo", "栽": "plantio", "調": "afinar", "域": "zona", "茂": "exuberante", "桟": "andamio", "減": "menguar", "式": "estilo", "威": "intimidar", "討": "reprender", "詠": "recitar", "城": "castillo", "諾": "consentimiento", "銭": "moneda", "弐": "ii (dos)", "訓": "instruccion", "誠": "sincero", "詩": "poesia", "試": "examen", "載": "cargar", "話": "hablar", "錠": "cerradura", "頻": "repetidamente", "題": "tema", "衣": "ropa", "歴": "curriculum", "定": "determinacion", "赴": "proceder", "装": "atuendo", "止": "detenerse", "誕": "natividad", "正": "correcto", "企": "emprender", "裏": "reverso", "証": "certificacion", "歩": "andar", "越": "adelantar", "壊": "demolicion", "賦": "recaudacion", "走": "correr", "渉": "vadear", "肯": "acuerdo", "婿": "novio", "建": "construir", "延": "prolongar", "政": "politica", "超": "sobrepasar", "裁": "confeccionar", "武": "guerrero", "礎": "piedra angular", "堤": "dique", "是": "debidamente", "遠": "distante", "制": "sistema", "滞": "estancado", "芸": "destreza", "天": "cielo", "幅": "rollo colgante", "製": "made in", "錦": "brocado", "帽": "sombrero", "市": "mercado", "布": "tela", "姉": "hermana mayor", "肺": "pulmones", "霜": "escarcha", "雷": "trueno", "初": "primera vez", "転": "girar", "帯": "faja", "猿": "mono", "帆": "vela", "幕": "cortina", "曇": "nublado", "冬": "invierno", "哀": "patetico", "幌": "baldaquin", "雲": "nube", "雨": "lluvia", "刺": "espina", "混": "mezclar", "匕": "cuchara", "喝": "ronco", "立": "en pie", "章": "insignia", "鐘": "campana", "謁": "audiencia", "帝": "soberano", "北": "norte", "皆": "todos", "褐": "marron", "童": "juvenil", "嫡": "esposa legitima", "瞳": "pupila", "泣": "llorar", "昆": "descendientes", "適": "apropiado", "滴": "gotear", "嬌": "atractiva", "比": "comparar", "競": "disputar", "背": "estatura", "脂": "grasa", "橋": "puente", "旨": "delicioso", "商": "hacer un trato", "渇": "sed", "敵": "enemigo", "識": "perspicaz", "腹": "abdomen", "鏡": "espejo", "歌": "cancion", "欠": "carencia", "毎": "todos los", "乞": "mendigar", "亡": "difunto", "資": "bienes", "諮": "consultar", "炊": "cocinar", "次": "siguiente", "軟": "blando", "梅": "ciruela", "姿": "figura", "複": "duplicar", "茨": "zarza", "乾": "sequia", "敏": "astucia", "暗": "oscuridad", "海": "mar", "壱": "i (uno)", "剖": "dividir", "培": "cultivar", "境": "limite", "音": "sonido", "賠": "compensacion", "吹": "soplar", "韻": "rima", "坊": "chiquillo", "県": "prefectura", "歳": "fin de año", "激": "violento", "鋭": "afilado", "荒": "arrasado", "賓": "V.I.P.", "妊": "embarazada", "凍": "helado", "望": "ambicion", "妄": "ilusion", "方": "direccion", "放": "liberar", "染": "teñir", "曽": "anteriormente", "棟": "caballete", "贈": "regalo", "訪": "visitar", "増": "aumento", "説": "rumor", "芳": "perfumado", "東": "este", "燃": "quemar", "盲": "ciego", "脱": "desnudarse", "廷": "tribunal", "妨": "obstaculizar", "肪": "obeso", "起": "despertar", "竜": "dragon", "逐": "cumplir", "栃": "castaña de Indias", "風": "viento", "豚": "puerco", "池": "estanque", "虫": "insecto", "電": "electricidad", "包": "envolver", "地": "terreno", "記": "escriba", "滝": "catarata", "蚕": "gusano de seda", "蛇": "serpiente", "独": "solitario", "蛍": "luciernaga", "蝶": "mariposa", "砲": "cañon", "亀": "tortuga de tierra", "虹": "arco iris", "遂": "consumar", "己": "el yo", "胞": "placenta", "泡": "burbuja", "妃": "reina", "改": "reforma", "進": "avanzar", "鮮": "fresco", "差": "distincion", "美": "belleza", "奪": "arrebatar", "湯": "agua caliente", "洋": "oceano", "詳": "detallado", "集": "reunir", "雑": "varios", "羊": "oveja", "確": "seguro", "礁": "arrecife", "着": "vestirse", "達": "habil", "羨": "envidia", "焦": "chamuscar", "場": "lugar", "准": "cuasi-", "腸": "intestinos", "奮": "excitado", "雌": "hembra", "家": "casa", "唯": "solo", "嫁": "novia", "豪": "abrumador", "準": "semi-", "床": "cama", "歓": "deleite", "庫": "garaje", "習": "aprender", "午": "mediodia", "曜": "dia de la semana", "心": "corazon", "店": "tienda", "忘": "olvidar", "翌": "subsecuente", "壇": "podio", "回": "veces", "困": "apuro", "固": "duro", "国": "pais", "観": "panorama", "曰": "dixit", "園": "parque", "団": "grupo", "権": "autoridad", "姻": "matrimonio", "麻": "cañamo", "庭": "patio", "羽": "plumas", "庁": "oficina gubernamental", "濯": "colada", "因": "causa", "許": "permitir", "磨": "pulir", "忙": "ocupado", "悦": "extasis", "志": "intencion", "串": "pinchito", "憎": "odio", "悟": "iluminacion", "忠": "lealtad", "応": "adaptar", "悔": "arrepentimiento", "悼": "lamento", "想": "concepto", "恒": "constancia", "惑": "engatusar", "寡": "viuda", "誌": "documento", "恐": "terror", "息": "respiracion", "忍": "aguante", "患": "afligido", "恩": "gracia", "忌": "velatorio", "憩": "pausa", "憂": "melancolia", "恵": "favor", "意": "idea", "認": "reconocer", "怖": "miedo", "感": "emocion", "思": "pensar", "慌": "desconcierto", "添": "anexo", "憾": "remordimiento", "摩": "rozar", "抄": "extracto", "抹": "frotar", "愉": "placer", "搭": "embarcar", "慕": "ansia", "看": "vigilar", "憶": "recuerdo", "抱": "abrazo", "拍": "aplaudir", "拓": "despejar (el terreno)", "招": "invitar", "泌": "rezumar", "打": "golpear", "手": "mano", "拘": "arrestar", "必": "necesariamente", "慣": "costumbre", "我": "ego", "犠": "sacrificio", "批": "critica", "義": "virtud", "議": "deliberacion", "抗": "confrontacion", "惰": "pereza", "慎": "humildad", "揚": "enarbolar", "接": "tocar", "鼻": "nariz", "械": "artilugio", "提": "propuesta", "戒": "mandamiento", "担": "llevar sobre los hombros", "財": "propiedad", "刑": "castigar", "存": "suponer", "拠": "apoyo", "推": "conjetura", "才": "genio", "持": "sostener", "摘": "pellizcar", "損": "daño", "描": "bosquejar", "括": "sujetar", "揮": "blandir", "掛": "colgar", "型": "molde", "拾": "recoger", "挑": "desafio", "指": "dedo", "操": "pilotar", "捨": "descartar", "研": "bruñir", "在": "existir", "材": "material", "掲": "subir", "拐": "secuestrar", "隻": "bajeles", "及": "alcanzar", "護": "custodiar", "抜": "zafarse", "吸": "chupar", "丈": "metraje", "友": "amigo", "更": "renovar", "投": "lanzar", "怒": "ira", "硬": "rigido", "奴": "tipejo", "枝": "leño", "技": "pericia", "殻": "cascara", "設": "establecimiento", "肢": "extremidad", "支": "rama", "吏": "funcionario", "扱": "manejar", "双": "par", "史": "historia", "撃": "azotar", "桑": "morera", "又": "o bien", "乃": "a partir de", "獲": "obtener", "携": "portatil", "没": "ahogarse", "茎": "tallo", "拡": "ampliar", "寂": "soledad", "督": "entrenador", "爪": "garras", "返": "devolver", "広": "ancho", "雄": "macho", "授": "impartir", "叔": "tio", "浮": "flotar", "乳": "leche", "採": "recolectar", "台": "pedestal", "販": "marketing", "軽": "liviano", "反": "anti-", "愛": "amor", "淑": "gracil", "将": "lider", "弁": "valvula", "受": "aceptar", "治": "reinar", "奨": "exhortar", "怠": "descuidar", "板": "tabla", "怪": "sospechoso", "妥": "amable", "坂": "pendiente", "払": "pagar", "菜": "verdura", "鉱": "mineral", "岐": "bifurcacion", "硫": "azufre", "崩": "derrumbarse", "山": "montaña", "撤": "eliminar", "始": "empezar", "到": "llegada", "去": "pasado", "峠": "cima de la montaña", "密": "oculto", "銃": "fusil", "致": "facer", "蜜": "miel", "育": "educar", "拙": "torpe", "炭": "carbon", "充": "asignar", "互": "mutuamente", "流": "corriente", "允": "licencia", "室": "sala", "至": "climax", "出": "salir", "岩": "roca", "法": "metodo", "胎": "matriz", "会": "reunion", "唆": "cautivar", "窓": "ventana", "棄": "abandonar", "分": "parte", "鉛": "plomo", "裕": "abundante", "容": "contener", "貧": "pobreza", "堂": "sala publica", "裳": "falda", "浴": "bañarse", "公": "publico", "翁": "anciano venerable", "嵐": "tormenta", "披": "exponer", "松": "pino", "婆": "abuelita", "党": "partido", "賞": "premio", "沿": "circunvalar", "欲": "anhelo", "込": "aglomeracion", "溶": "derretir", "谷": "valle", "常": "normal", "崎": "promontorio", "皮": "pellejo", "被": "incurrir", "頒": "particion", "訟": "querellarse", "破": "desgarrar", "掌": "manipular", "入": "entrar", "波": "olas", "敢": "osadia", "最": "maximo", "殖": "multiplicarse", "撮": "tomar fotos", "漫": "suelto", "耳": "oreja", "濁": "turbio", "殊": "particularmente", "烈": "ardiente", "環": "anillo", "残": "el resto", "裂": "ruptura", "葬": "funeral", "聴": "escuchar", "恥": "vergüenza", "買": "comprar", "列": "hilera", "趣": "lo esencial", "死": "muerte", "置": "colocar", "懐": "bolsillo", "殉": "martirio", "職": "puesto", "還": "mandar de vuelta", "罰": "reprender", "寧": "mas bien", "取": "tomar", "聖": "sagrado", "瞬": "pestañeo", "慢": "ridiculo", "功": "exito", "臓": "entrañas", "姫": "princesa", "加": "añadir", "渓": "arroyo de montaña", "臣": "criado", "規": "estandar", "励": "animar", "鉄": "hierro", "募": "reclutar", "臨": "expectacion", "劣": "inferioridad", "夫": "marido", "蔵": "almacen", "失": "perder", "労": "fatiga", "潜": "sumergir", "賛": "estar de acuerdo", "替": "canje", "賢": "inteligente", "扶": "asistencia", "拒": "repeler", "勧": "persuadir", "努": "esfuerzo", "覧": "ojear", "力": "fuerza", "堅": "estricto", "巨": "gigantesco", "男": "varon", "迭": "alternar", "徹": "penetrar", "徳": "benevolencia", "賀": "felicitaciones", "役": "funcion", "従": "seguir", "稿": "borrador", "往": "trayecto", "得": "ganancia", "脇": "axila", "脅": "amenaza", "懲": "penal", "協": "co-", "衡": "equilibrio", "征": "subyugar", "彼": "el", "税": "impuesto", "復": "restaurar", "徴": "indicios", "待": "esperar", "徒": "alumno", "架": "erigir", "行": "ir", "微": "delicado", "街": "bulevar", "律": "ritmico", "稼": "ingresos", "径": "diametro", "程": "alcance", "秘": "secreto", "委": "comite", "秒": "segundo", "愁": "tristeza", "穫": "cosecha", "菌": "germen", "移": "trasladar", "稲": "planta del arroz", "秋": "otoño", "香": "incienso", "季": "estaciones del año", "粒": "granos", "穂": "espiga", "梨": "peral", "誘": "tentar", "利": "beneficio", "透": "transparente", "穀": "cereales", "称": "apelacion", "秀": "sobresaliente", "私": "privado", "粘": "pegajoso", "米": "arroz", "粧": "cosmetico", "稚": "inmaduro", "粉": "harina", "秩": "regularidad", "和": "armonia", "迷": "desviacion", "類": "tipo de", "求": "solicitud", "人": "persona", "筒": "cilindro", "笑": "risa", "算": "calcular", "漆": "laca", "策": "estratagema", "築": "fabricar", "救": "salvacion", "様": "don", "菊": "crisantemo", "笠": "sombrero de bambu", "粋": "chic", "糧": "provisiones", "佐": "asistente", "答": "solucion", "筆": "pincel de escritura", "筋": "musculo", "球": "balon", "等": "etc.", "箱": "caja", "竹": "bambu", "楼": "atalaya", "笹": "bambu enano", "但": "sin embargo", "奥": "hondura", "数": "numero", "簿": "registrar", "依": "confiar", "仏": "Buda", "佳": "excelente", "健": "saludable", "僧": "monje budista", "位": "rango", "件": "caso", "住": "habitar", "仮": "provisional", "停": "parada", "伯": "conde", "伏": "postrado", "偵": "espiar", "値": "precio", "信": "fe", "体": "cuerpo", "他": "otro", "仕": "atender", "侍": "camarero", "休": "descanso", "悠": "remoto", "側": "lado", "倣": "emular", "例": "ejemplo", "倒": "derrocamiento", "俗": "vulgar", "仲": "intermediario", "伝": "transmitir", "個": "individual", "仁": "humanitario", "符": "simbolo", "億": "cien millones", "償": "indemnizacion", "褒": "alabar", "袋": "saco", "傷": "herida", "保": "conservar", "伐": "talar", "仙": "ermitaño", "貸": "prestar", "傑": "grandeza", "賃": "paga", "使": "usar", "催": "anfitrion", "儀": "ceremonia", "付": "adherir", "宿": "hostal", "侮": "mofarse", "任": "responsabilidad", "便": "conveniencia", "優": "ternura", "化": "cambio", "代": "sustituto", "花": "flor", "府": "municipio", "倍": "doble", "併": "juntar", "年": "año", "内": "dentro", "貨": "carga", "似": "semejante", "傾": "inclinar", "瓦": "teja", "以": "por medio de", "丙": "tercera clase", "柄": "diseño", "営": "ocupacion", "腐": "podrirse", "畝": "surco", "久": "duradero", "肉": "carne", "宮": "templo sintoista", "善": "bondad", "何": "que", "俊": "sagaz", "傍": "miron", "卒": "graduarse", "座": "sentarse", "囚": "capturado", "荷": "equipaje", "傘": "paraguas", "瓶": "florero", "匁": "monme", "喚": "alarido", "夜": "vespertino", "液": "liquido", "履": "calzado", "掘": "excavar", "塚": "monticulo", "尿": "orina", "賜": "otorgar", "握": "asir", "施": "limosna", "弊": "abuso", "屋": "tejado", "換": "intercambio", "堀": "zanja", "幣": "en metalico", "塀": "cercado", "旋": "rotacion", "融": "disolver", "居": "residir", "勿": "no", "易": "facil", "泥": "barro", "遊": "jugar", "物": "cosa", "尼": "monja", "旅": "viaje", "屈": "ceder", "祥": "favorable", "顧": "mirar atras", "昼": "de dia", "肩": "hombro", "啓": "manifestar", "房": "borla", "遅": "lento", "尽": "agotar", "尺": "shaku", "示": "mostrar", "戻": "volver", "涙": "lagrima", "祝": "celebrar", "局": "oficina", "沢": "cienaga", "雇": "contratar", "択": "escoger", "層": "estrato", "戸": "puerta", "漏": "filtracion", "礼": "saludo", "炉": "lar", "据": "establecer", "扇": "ventilador", "訳": "traducir", "刷": "imprimir", "油": "aceite", "禁": "prohibicion", "軸": "eje", "視": "inspeccion", "宙": "espacio", "抽": "extraer", "祭": "festividad", "襟": "cuello de la camisa", "崇": "adorar", "岬": "lengua de tierra", "福": "bendicion", "奈": "Nara", "笛": "silbato", "宗": "religion", "挿": "insertar", "擦": "rallar", "袖": "manga", "察": "estimacion", "款": "buena voluntad", "社": "empresa", "尉": "oficial militar", "甲": "coraza", "押": "empujar", "届": "repartir", "慰": "consuelo", "祉": "bienestar", "由": "por lo que", "詐": "mentira", "果": "fruta", "逝": "expirar", "斥": "rechazar", "雪": "nieve", "作": "realizar", "析": "tronchar", "漸": "gradualmente", "神": "dioses", "誓": "juramento", "斤": "hacha", "伸": "expandir", "折": "plegar", "断": "recortar", "訴": "acusacion", "申": "tomar la palabra", "裸": "desnudo", "暫": "temporalmente", "菓": "caramelo", "近": "cerca", "昨": "ayer", "祈": "orar", "所": "sitio", "質": "sustancia", "課": "capitulo", "哲": "filosofia", "捜": "buscar", "群": "manada", "侵": "invadir", "君": "tu", "唐": "Tang", "掃": "barrer", "糖": "azucar", "儒": "confuciano", "需": "demanda", "端": "margen", "満": "lleno", "穏": "calma", "争": "contienda", "急": "apresurarse", "寝": "yacer", "逮": "aprehender", "耐": "a prueba de", "浸": "inmersion", "浄": "limpio", "伊": "Italia", "婦": "señora", "画": "trazo de pincel", "事": "asunto", "当": "acertar", "両": "ambos", "尋": "encuesta", "康": "sano", "録": "grabar", "庶": "plebeyo", "料": "importe", "措": "apartar", "昔": "erase una vez", "用": "utilizar", "曲": "doblegar", "遮": "interceptar", "度": "grado", "噴": "erupcion", "備": "equipamiento", "錯": "confuso", "曹": "cadete", "歯": "diente", "奔": "bullicio", "渡": "cruzar", "科": "departamento", "遭": "encuentro", "槽": "tinaja", "借": "tomar prestado", "廿": "veinte", "庸": "confortable", "席": "asiento", "漕": "remar", "散": "esparcer", "惜": "pena", "斗": "Osa Mayor", "図": "mapa", "知": "saber", "杯": "una taza de", "券": "boleto", "否": "negar", "暁": "alba", "焼": "freir", "謄": "facsimil", "乏": "destitucion", "墳": "sepulcro", "芝": "cesped", "半": "mitad", "巻": "pergamino", "勝": "victoria", "智": "sabiduria", "矯": "rectificar", "之": "de", "憤": "indignacion", "矢": "dardo", "不": "negativo", "判": "sentencia", "畔": "borde de un arrozal", "族": "tribu", "版": "bloque de imprenta", "圏": "esfera", "伴": "consorte", "藤": "glicina", "片": "un lado", "帰": "volver a casa", "汚": "sucio", "朽": "decadencia", "矛": "alabarda", "身": "alguien", "誇": "jactarse", "写": "copiar", "柔": "tierno", "与": "conceder", "班": "brigada", "弘": "extenso", "老": "anciano", "弓": "arco", "務": "tarea", "弱": "debil", "引": "tirar", "強": "fuerte", "号": "apodo", "沸": "hervir", "第": "Num.", "費": "gastos", "弟": "hermano menor", "弔": "pesame", "霧": "niebla", "謝": "disculparse", "射": "disparar", "巧": "habilidad", "較": "contraste", "渚": "ribera", "追": "perseguir", "賭": "apostar", "猪": "jabali", "峡": "desfiladero", "孝": "devocion filial", "狭": "estrecho", "煮": "cocer", "者": "alguno", "官": "burocrata", "師": "experto", "暑": "bochorno", "教": "enseñar", "校": "escuela", "考": "considerar", "効": "merito", "父": "padre", "挟": "intercalar", "拷": "tortura", "署": "firma", "諸": "diversos", "交": "entremezclar", "著": "celebre", "帥": "comandante", "管": "cañeria", "棺": "ataud", "躍": "salto", "陽": "luz del sol", "足": "pie", "促": "estimular", "跳": "brinco", "随": "ir detras", "髄": "medula", "践": "pisar", "陳": "poner en fila", "防": "defenderse de", "渦": "remolino", "阪": "Alto", "禍": "calamidad", "際": "ocasion", "滑": "resbaladizo", "路": "sendero", "附": "acoplado", "阿": "africa", "院": "Institucion", "距": "larga distancia", "過": "demasiado", "障": "obstruir", "骨": "esqueleto", "踏": "paso", "陪": "auxiliar", "露": "rocio", "窒": "obturar", "降": "descender", "窯": "horno", "陣": "campamento", "控": "retener", "丘": "cerro", "空": "vacio", "堕": "degenerar", "突": "punzar", "階": "piso", "岳": "colina", "隊": "regimiento", "探": "tantear", "窮": "pauperrimo", "深": "profundo", "搾": "estrujar", "究": "indagacion", "兵": "soldado", "隣": "vecino", "隔": "aislar", "窃": "sigiloso", "穴": "agujero", "窪": "depresion", "陛": "alteza", "墜": "caida", "隠": "encubrir", "陥": "colapso", "給": "salario", "羅": "gasa", "結": "atar", "織": "tejer", "紡": "hilatura", "絡": "entrelazar", "線": "linea", "絞": "estrangular", "維": "fibra", "納": "concluir", "級": "clase", "紅": "carmin", "繁": "lujo", "締": "estrechar", "繕": "remendar", "続": "continuar", "紛": "perturbar", "統": "integracion", "終": "final", "縦": "vertical", "縮": "encoger", "浜": "costa", "絵": "dibujo", "糸": "hilo", "練": "practicar", "紀": "cronica", "緒": "correa", "紫": "purpura", "幾": "cuantos", "畜": "ganado", "索": "cable", "綿": "algodon", "後": "detras", "緑": "verde", "緊": "tenso", "継": "heredar", "総": "general", "細": "delgado", "紳": "caballero", "縛": "amarrar", "絹": "seda", "機": "mecanismo", "網": "red", "繰": "enrollado", "幼": "infancia", "縁": "afinidad", "縄": "cuerda de paja", "紹": "presentar a alguien", "約": "promesa", "幽": "impreciso", "経": "sðtra", "蓄": "acaudalar", "玄": "misterioso", "累": "acumular", "御": "honorable", "令": "ordenes", "却": "al contrario", "孫": "nieto", "勇": "coraje", "冷": "frescura", "弦": "cuerda de arco", "係": "encargado", "擁": "abarcar", "懸": "suspender", "滋": "nutritivo", "鈴": "campanilla", "犯": "crimen", "疑": "duda", "脚": "espinilla", "凝": "solidificar", "擬": "imitar", "踊": "bailar", "卸": "al por mayor", "範": "patron", "零": "cero", "領": "jurisdiccion", "慈": "piedad", "磁": "iman", "齢": "edad", "系": "linaje", "通": "trafico", "命": "destino", "服": "prenda", "尊": "reverencia", "短": "corto", "酬": "recompensar", "留": "estacionar", "酉": "signo del pajaro", "酔": "borracho", "腕": "brazo", "酌": "servir sake", "猶": "vacilar", "貿": "comerciar", "頭": "cabeza", "危": "peligroso", "酷": "crueldad", "豆": "alubias", "柳": "sauce", "厄": "mala suerte", "印": "sello", "卵": "huevo", "配": "distribuir", "苑": "jardin", "興": "entretener", "酵": "fermentacion", "宛": "direccion postal", "豊": "provechoso", "怨": "rencor", "酪": "productos lacteos", "酢": "vinagre", "鼓": "tambor", "酒": "sake", "酸": "acido", "爵": "baron", "濫": "desbordarse", "盗": "robar", "盛": "auge", "盆": "cuenca", "銀": "plata", "恨": "resentimiento", "血": "sangre", "節": "nodulo", "飯": "comida", "皿": "plato", "即": "instantaneo", "食": "comer", "朗": "melodioso", "浪": "errante", "喜": "alegria", "飢": "hambriento", "娘": "hija", "眼": "globo ocular", "限": "confin", "退": "retirada", "監": "supervisar", "鑑": "especimen", "飲": "beber", "樹": "arboles madereros", "盟": "alianza", "良": "bueno", "猛": "fiero", "根": "raiz", "塩": "sal", "温": "caliente", "概": "aproximadamente", "飾": "decorar", "坪": "area de dos esteras", "館": "Edificio", "凶": "villano", "鈍": "embotado", "新": "nuevo", "梓": "catalpa", "離": "desprenderse", "幸": "felicidad", "純": "genuino", "胸": "pecho", "親": "progenitor", "薪": "leña", "飽": "harto", "壁": "pared", "評": "evaluacion", "養": "fomentar", "餓": "inanicion", "避": "refugiarse", "殺": "matar", "希": "esperanza", "辞": "dimitir", "慨": "deplorar", "既": "previamente", "辛": "picante", "刈": "segar", "宰": "administrar", "呼": "llamar", "平": "llano", "嬢": "muchacha", "陸": "terrestre", "劾": "denunciar", "精": "refinado", "糾": "retorcer", "述": "mencionar", "術": "arte", "麦": "cebada", "請": "solicito", "醸": "destilacion", "青": "azul", "菱": "diamante", "素": "elemental", "壌": "parcela", "碑": "lapida", "執": "tenaz", "叫": "grito", "寒": "frio", "該": "mencionado anteriormente", "刻": "cincelar", "報": "informe", "核": "nucleo", "譲": "deferencia", "亥": "signo del jabali", "毒": "veneno", "卑": "despreciable", "収": "rentas", "睦": "intimo", "陵": "mausoleo", "勢": "fuerzas", "熱": "calor", "割": "proporcion", "責": "inculpar", "生": "vida", "喫": "consumir", "績": "hazaña", "静": "apacible", "星": "estrella", "晴": "despejado", "契": "compromiso", "隆": "giba", "債": "fianza", "拝": "venerar", "憲": "constitucion", "轄": "control", "表": "superficie", "産": "produccion", "姓": "apellido", "峰": "cumbre", "俵": "bolsa", "牲": "sacrificio animal", "潔": "inmaculado", "漬": "escabeche", "情": "sentimientos", "害": "damnificar", "縫": "coser", "清": "puro", "性": "sexo", "積": "volumen", "念": "deseo", "春": "primavera", "奉": "dedicar", "乗": "montar", "華": "esplendor", "椿": "camelia", "今": "ahora", "剰": "exceso", "吟": "versificar", "棒": "cayado", "嘆": "suspiro", "鋳": "fundir", "籍": "inscribirse", "勤": "diligencia", "泰": "pacifico", "寿": "longevidad", "奏": "tocar musica", "謹": "discreto", "実": "realidad", "俸": "estipendio", "睡": "somnoliento", "難": "dificil", "含": "incluir", "錘": "huso", "垂": "pender", "漢": "Sino-", "標": "señal", "遷": "transicion", "票": "voto", "廉": "ganga", "栗": "castaño", "謙": "modesto", "陰": "penumbra", "門": "verja", "野": "llanura", "兼": "al mismo tiempo", "預": "deposito", "序": "prefacio", "漂": "a la deriva", "南": "sur", "予": "de antemano", "価": "valor", "鎌": "hoz", "要": "necesitar", "嫌": "desagradar", "煙": "humo", "腰": "caderas", "楠": "alcanforero", "献": "donacion", "琴": "arpa", "問": "pregunta", "覆": "volcar", "西": "oeste", "潤": "mojado", "開": "abierto", "閲": "pasar revista", "俳": "haiku", "輩": "camarada", "侯": "marques", "簡": "sencillo", "倉": "granero", "罪": "culpabilidad", "違": "diferencia", "排": "repudiar", "非": "sin", "偉": "admirable", "閣": "torre", "聞": "oir", "間": "intervalo", "快": "alegre", "決": "decidir", "闘": "lucha", "扉": "puerta principal", "欄": "columna tipografica", "悲": "triste", "閥": "camarilla", "創": "genesis", "候": "clima", "閉": "cerrado", "閑": "ocio", "途": "ruta", "余": "excesivo", "整": "organizar", "徐": "progresivamente", "叙": "conferir", "肝": "higado", "勅": "orden imperial", "頼": "confianza", "塗": "pintura", "束": "manojo", "刊": "publicacion", "韓": "Corea", "宇": "universo", "速": "rapido", "軒": "alero", "緯": "horizontal", "衛": "defensa", "除": "excluir", "汗": "sudor", "干": "secar", "幹": "tronco del arbol", "岸": "playa", "斜": "diagonal", "瀬": "rapidos", "剣": "sable", "芋": "patata", "疎": "enajenar", "働": "trabajar", "疫": "epidemia", "検": "test", "枢": "bisagra", "痘": "viruela", "症": "sintomas", "険": "escarpado", "勲": "proeza meritoria", "痢": "diarrea", "匿": "esconderse", "倹": "frugal", "重": "pesado", "動": "mover", "薫": "fragante", "医": "medico", "癖": "tic", "匠": "artesano", "疲": "cansado", "痛": "dolor", "衝": "chocar", "種": "especie", "痴": "estupido", "匹": "igual", "疾": "raudamente", "病": "enfermo", "区": "distrito", "澄": "resplandeciente", "膨": "hincharse", "迎": "bienvenido", "惨": "desventurado", "僚": "colega", "形": "forma", "寮": "residencia", "診": "chequeo", "廃": "abolicion", "療": "terapia", "欧": "Europa", "修": "disciplina", "殴": "asalto", "抑": "reprimir", "発": "partida", "杉": "cedro", "顔": "cara", "彩": "colorear", "参": "presenciar", "彫": "esculpir", "彰": "patente", "影": "sombra", "須": "deber", "彦": "chico", "珍": "raro", "登": "ascender", "仰": "boca arriba", "済": "terminar", "恋": "romance", "対": "frente a frente", "渋": "astringente", "粛": "solemne", "斉": "simetrico", "蛮": "barbaro", "文": "oracion", "蚊": "mosquito", "央": "centro", "跡": "rastro", "斎": "purificacion", "剤": "dosis", "率": "porcentaje", "英": "Inglaterra", "摂": "delegado", "赦": "perdon", "楽": "musica", "赤": "rojo", "変": "insolito", "塁": "bases", "薬": "medicina", "湾": "golfo", "映": "reflejar", "紋": "blason familiar", "黄": "amarillo", "甚": "enormemente", "組": "asociacion", "無": "nada", "勘": "intuicion", "堪": "resistir", "紺": "azul marino", "謀": "conspirar", "色": "color", "旗": "bandera nacional", "舞": "revoltear", "甘": "dulce", "貴": "precioso", "把": "agarrar", "棋": "trebejo", "某": "fulanito de tal", "碁": "go", "遣": "despachar", "絶": "discontinuo", "期": "periodo", "肥": "fertilizante", "遺": "legar", "粗": "burdo", "艶": "satinado", "欺": "timo", "横": "de soslayo", "基": "cimientos", "祖": "antepasado", "媒": "mediador", "租": "tarifa", "湿": "humedo", "暴": "explosion", "港": "puerto", "囲": "rodear", "畳": "estera tatami", "顕": "manifiesto", "共": "juntos", "恭": "cortesia", "譜": "partitura", "阻": "estorbo", "僕": "servidor", "並": "fila", "殿": "Sr.", "異": "singular", "洪": "anegar", "宜": "saludos cordiales", "査": "investigar", "業": "profesion", "爆": "bomba", "選": "eleccion", "助": "ayuda", "供": "entregar", "霊": "espiritu", "耕": "labrar", "繊": "esbelto", "普": "universal", "井": "pozo", "翼": "ala", "撲": "abofetear", "底": "fondo", "構": "postura", "編": "recopilacion", "抵": "rebatir", "眠": "dormir", "浦": "bahia", "悪": "malo", "遍": "omnipresente", "冊": "tomo", "購": "suscripcion", "典": "codigo", "円": "circulo", "氏": "nombre de familia", "婚": "casarse", "亜": "Asia", "紙": "papel", "捕": "capturar", "講": "conferencia", "蒲": "anea", "民": "gente", "偏": "parcialidad", "再": "de nuevo", "輪": "rueda", "溝": "canal", "倫": "etica", "触": "contacto", "解": "solucionar", "角": "angulo", "低": "rebajar", "論": "argumento", "廊": "pasillo", "部": "seccion", "鍛": "forjar", "衆": "muchedumbre", "脈": "vena", "幻": "fantasma", "郊": "afueras", "飼": "domesticar", "詞": "categoria gramatical", "逓": "servicio postal", "郵": "correo", "郡": "comarca", "盾": "escudo", "郷": "tierra natal", "循": "secuencial", "郭": "contorno", "嗣": "sucesor", "派": "faccion", "伺": "presentar sus respetos", "舗": "comercio", "響": "eco", "司": "director", "都": "metropolis", "補": "suplemento", "后": "emperatriz", "郎": "hijo", "段": "gradacion", "邸": "mansion", "邦": "patria", "舟": "bote", "来": "venir", "飛": "volar", "暇": "tiempo libre", "妻": "esposa", "気": "energia", "舶": "buque mercante", "靴": "zapatos", "声": "voz", "航": "navegar", "盤": "bandeja", "艇": "barca de remos", "艦": "acorazado", "沈": "hundirse", "汽": "vapor", "繭": "capullo", "搬": "acarrear", "衷": "interior", "船": "barco", "衰": "declive", "瓜": "melon", "面": "mascara", "覇": "hegemonia", "弧": "curvatura", "般": "carguero", "益": "redito", "敷": "extender", "孤": "huerfanof", "革": "cuero", "函": "cajon", "脹": "dilatar", "牙": "colmillo", "髪": "pelo", "娯": "diversion", "蒸": "vaho", "長": "largo", "極": "polos", "誤": "error", "尾": "cola de animal", "展": "desarrollar", "偽": "falsedad", "番": "turno", "帳": "cuaderno de apuntes", "呉": "dar", "雅": "elegante", "耗": "gastar", "毛": "pelaje", "為": "hacer", "宅": "domicilio", "承": "consentir", "翻": "voltear", "審": "vista", "芽": "germinar", "託": "consignar", "張": "alargar", "釈": "explicacion", "藩": "clan", "邪": "infame", "桜": "cerezo", "烏": "cuervo", "巣": "nido", "鳩": "paloma", "鳴": "piar", "鶴": "grulla", "猟": "caceria", "媛": "bella mujer", "弾": "bala", "厳": "severo", "戦": "guerra", "鳥": "pajaro", "獣": "animal", "嘱": "encomendar", "偶": "por casualidad", "援": "socorro", "島": "isla", "属": "pertenecer", "禅": "zen", "誉": "reputacion", "単": "simple", "悩": "inquietud", "緩": "flojear", "鎖": "cadena", "鶏": "gallina", "暖": "calidez", "挙": "alzar", "脳": "cerebro", "喪": "luto", "蔦": "parra", "験": "verificacion", "缶": "lata", "懇": "sociable", "揺": "mecerse", "免": "excusarse", "隅": "esquina", "謡": "cancion de nõ", "象": "elefante", "墾": "abrir tierras", "愚": "alocado", "像": "estatua", "遇": "entrevista", "塑": "modelar", "晩": "crepusculo", "逸": "eludir", "駒": "potro", "剛": "vigoroso", "勉": "ejercer", "就": "concerniente a", "綱": "soga", "陶": "alfareria", "鋼": "acero", "馬": "caballo", "逆": "invertido", "岡": "Monte", "篤": "ferviente", "寅": "signo del tigre", "慮": "prudencia", "虚": "vacuo", "騰": "inflacion", "戯": "jolgorio", "鹿": "ciervo", "駄": "oneroso", "熊": "oso", "麗": "hermoso", "騎": "ecuestre", "態": "actitud", "虜": "cautivo", "駆": "conducir", "慶": "jubilacion", "駐": "aparcar", "膚": "dermis", "薦": "recomendar", "劇": "drama", "虐": "opresion"}
HeisigEn = {'一': 'one', '二': 'two', '三': 'three', '四': 'four', '五': 'five', '六': 'six', '七': 'seven', '八': 'eight', '九': 'nine', '十': 'ten', '口': 'mouth', '日': 'day', '月': 'month', '田': 'rice field', '目': 'eye', '古': 'old', '吾': 'I', '冒': 'risk', '朋': 'companion', '明': 'bright', '唱': 'chant', '晶': 'sparkle', '品': 'goods', '呂': 'spine', '昌': 'prosperous', '早': 'early', '旭': 'rising sun', '世': 'generation', '胃': 'stomach', '旦': 'nightbreak', '胆': 'gall bladder', '亘': 'span', '凹': 'concave', '凸': 'convex', '旧': 'olden times', '自': 'oneself', '白': 'white', '百': 'hundred', '中': 'in', '千': 'thousand', '舌': 'tongue', '升': 'measuring box', '昇': 'rise up', '丸': 'round', '寸': 'measurement', '専': 'specialty', '博': 'Dr.', '卜': 'divining rod', '占': 'fortune-telling', '上': 'above', '下': 'below', '卓': 'eminent', '朝': 'morning', '只': 'only', '貝': 'shellfish', '貞': 'upright', '員': 'employee', '見': 'see', '児': 'newborn babe', '元': 'beginning', '頁': 'page', '頑': 'stubborn', '凡': 'mediocre', '負': 'defeat', '万': 'ten thousand', '句': 'phrase', '肌': 'texture', '旬': 'decameron', '勺': 'ladle', '的': "bull's eye", '首': 'neck', '乙': 'fish guts', '乱': 'riot', '直': 'straightaway', '具': 'tool', '真': 'true', '工': 'craft', '左': 'left', '右': 'right', '有': 'possess', '賄': 'bribe', '貢': 'tribute', '項': 'paragraph', '刀': 'sword', '刃': 'blade', '切': 'cut', '召': 'seduce', '昭': 'shining', '則': 'rule', '副': 'vice-', '別': 'separate', '丁': 'street', '町': 'town', '可': 'can', '頂': 'place on the head', '子': 'child', '孔': 'cavity', '了': 'complete', '女': 'woman', '好': 'fond', '如': 'likeness', '母': 'mama', '貫': 'pierce', '兄': 'elder brother', '克': 'overcome', '小': 'little', '少': 'few', '大': 'large', '多': 'many', '夕': 'evening', '汐': 'eventide', '外': 'outside', '名': 'name', '石': 'stone', '肖': 'resemblance', '硝': 'nitrate', '砕': 'smash', '砂': 'sand', '削': 'plane', '光': 'ray', '太': 'plump', '器': 'utensil', '臭': 'stinking', '妙': 'exquisite', '省': 'focus', '厚': 'thick', '奇': 'strange', '川': 'stream', '州': 'state', '順': 'obey', '水': 'water', '氷': 'icicle', '永': 'eternity', '泉': 'spring', '原': 'meadow', '願': 'petition', '泳': 'swim', '沼': 'marsh', '沖': 'open sea', '江': 'creek', '汁': 'soup', '潮': 'tide', '源': 'source', '活': 'lively', '消': 'extinguish', '況': 'but of course', '河': 'river', '泊': 'overnight', '湖': 'lake', '測': 'fathom', '土': 'soil', '吐': 'spit', '圧': 'pressure', '埼': 'cape', '垣': 'hedge', '圭': 'square jewel', '封': 'seal', '涯': 'horizon', '寺': 'Buddhist temple', '時': 'time', '均': 'level', '火': 'fire', '炎': 'inflammation', '煩': 'anxiety', '淡': 'thin', '灯': 'lamp', '畑': 'farm', '災': 'disaster', '灰': 'ashes', '点': 'spot', '照': 'illuminate', '魚': 'fish', '漁': 'fishing', '里': 'ri', '黒': 'black', '墨': 'black ink', '鯉': 'carp', '量': 'quantity', '厘': 'rin', '埋': 'bury', '同': 'same', '洞': 'den', '胴': 'trunk', '向': 'yonder', '尚': 'esteem', '字': 'character', '守': 'guard', '完': 'perfect', '宣': 'proclaim', '宵': 'wee hours', '安': 'relax', '宴': 'banquet', '寄': 'draw near', '富': 'wealth', '貯': 'savings', '木': 'tree', '林': 'grove', '森': 'forest', '桂': 'Japanese Judas-tree', '柏': 'oak', '枠': 'frame', '梢': 'treetops', '棚': 'shelf', '杏': 'apricot', '桐': 'paulownia', '植': 'plant', '枯': 'wither', '朴': 'crude', '村': 'village', '相': 'inter-', '机': 'desk', '本': 'book', '札': 'tag', '暦': 'calendar', '案': 'plan', '燥': 'parch', '未': 'not yet', '末': 'extremity', '沫': 'splash', '味': 'flavor', '妹': 'younger sister', '朱': 'vermilion', '株': 'stocks', '若': 'young', '草': 'grass', '苦': 'suffering', '寛': 'tolerant', '薄': 'dilute', '葉': 'leaf', '模': 'imitation', '漠': 'vague', '墓': 'grave', '暮': 'livelihood', '膜': 'membrane', '苗': 'seedling', '兆': 'portent', '桃': 'peach tree', '眺': 'stare', '犬': 'dog', '状': 'status quo', '黙': 'silence', '然': 'sort of thing', '荻': 'reed', '狩': 'hunt', '猫': 'cat', '牛': 'cow', '特': 'special', '告': 'revelation', '先': 'before', '洗': 'wash', '介': 'jammed in', '界': 'world', '茶': 'tea', '合': 'fit', '塔': 'pagoda', '王': 'king', '玉': 'jewel', '宝': 'treasure', '珠': 'pearl', '現': 'present', '狂': 'lunatic', '皇': 'emperor', '呈': 'display', '全': 'whole', '栓': 'plug', '理': 'logic', '主': 'lord', '注': 'pour', '柱': 'pillar', '金': 'gold', '銑': 'pig-iron', '鉢': 'bowl', '銅': 'copper', '釣': 'angling', '針': 'needle', '銘': 'inscription', '鎮': 'tranquilize', '道': 'road-way', '導': 'guidance', '辻': 'crossing', '迅': 'swift', '造': 'create', '迫': 'urge', '逃': 'escape', '辺': 'environs', '巡': 'patrol', '車': 'car', '連': 'take along', '軌': 'rut', '輸': 'transport', '前': 'in front', '各': 'each', '格': 'status', '略': 'abbreviation', '客': 'guest', '額': 'forehead', '夏': 'summer', '処': 'dispose', '条': 'twig', '落': 'fall', '冗': 'superfluous', '軍': 'army', '輝': 'radiance', '運': 'carry', '冠': 'crown', '夢': 'dream', '坑': 'pit', '高': 'tall', '享': 'receive', '塾': 'cram school', '熟': 'mellow', '亭': 'pavilion', '京': 'capital', '涼': 'refreshing', '景': 'scenery', '鯨': 'whale', '舎': 'cottage', '周': 'circumference', '週': 'week', '士': 'gentleman', '吉': 'good luck', '壮': 'robust', '荘': 'villa', '売': 'sell', '学': 'Study', '覚': 'Memorize', '栄': 'Flourish', '書': 'Write', '津': 'Haven', '牧': 'Breed', '攻': 'Aggression', '敗': 'Failing', '枚': 'Sheet', '故': 'Chance', '敬': 'Awe', '言': 'Says', '警': 'Admonish', '計': 'Plot', '獄': 'Prison', '訂': 'Revision', '討': 'Chastise', '訓': 'Instruction', '詔': 'Imperial Decree', '詰': 'Packed', '話': 'Tale', '詠': 'Recitation', '詩': 'Poem', '語': 'Language', '読': 'Read', '調': 'Tune', '談': 'Discussion', '諾': 'Consent', '諭': 'Rebuked', '式': 'Stylish', '試': 'Test', '弐': 'II', '域': 'Range', '賊': 'Burglar', '栽': 'Plantation', '載': 'Load', '茂': 'Overgrown', '成': 'Change into', '城': 'Castle', '誠': 'Sincere', '威': 'Intimidates', '滅': 'Destroys', '減': 'Reduce', '桟': 'Scaffold', '銭': 'Coin', '浅': 'Shallow', '止': 'Stop', '歩': 'Walk', '渉': 'To cross', '頻': 'Repeatedly', '肯': 'Agreement', '企': 'Undertakes', '歴': 'Curriculum', '武': 'Warrior', '賦': 'Levy', '正': 'correct', '証': 'evidence', '政': 'politics', '定': 'determination', '錠': 'lock', '走': 'run', '超': 'transcend', '赴': 'proceed', '越': 'surpass', '是': 'just so', '題': 'topic', '堤': 'embankment', '建': 'build', '延': 'prolong', '誕': 'nativity', '礎': 'cornerstone', '婿': 'bridegroom', '衣': 'clothing', '裁': 'tailor', '装': 'attire', '裏': 'back', '壊': 'demolition', '哀': 'pathetic', '遠': 'distance', '猿': 'monkey', '初': 'first time', '布': 'linen', '帆': 'sail', '幅': 'hanging scroll', '帽': 'cap', '幕': 'curtain', '幌': 'canopy', '錦': 'brocade', '市': 'market', '姉': 'elder sister', '肺': 'lungs', '帯': 'sash', '滞': 'stagnant', '刺': 'thorn', '制': 'system', '製': 'made in', '転': 'revolve', '芸': 'technique', '雨': 'rain', '雲': 'cloud', '曇': 'cloudy weather', '雷': 'thunder', '霜': 'frost', '冬': 'winter', '天': 'heaven', '橋': 'bridge', '嬌': 'attractive', '立': 'standing up', '泣': 'crying', '章': 'badge', '競': 'vie', '帝': 'sovereign', '童': 'juvenile', '瞳': 'pupil', '鐘': 'bell', '商': 'make a deal', '嫡': 'legitimate wife', '適': 'suitable', '滴': 'drips', '敵': 'enemy', 'ヒ': 'spoon', '北': 'north', '背': 'stature', '比': 'compare', '昆': 'descendants', '皆': 'all', '混': 'mix', '渇': 'thirst', '謁': 'audience', '褐': 'brown', '喝': 'hoarse', '旨': 'delicious', '脂': 'fat', '壱': 'I (roman numeral)', '每': 'every', '敏': 'clever', '梅': 'plum', '海': 'sea', '乞': 'begging', '乾': 'drought', '腹': 'abdomen', '複': 'duplicate', '欠': 'lack', '吹': 'blowing', '炊': 'cooks', '歌': 'song', '軟': 'soft', '次': 'next', '茨': 'wild rose', '資': 'assets', '諮': 'consult with', '賠': 'compensate', '培': 'cultivate', '剖': 'division', '音': 'sound', '暗': 'darkness', '韻': 'rhyme', '識': 'discriminated', '鏡': 'mirror', '境': 'boundary', '亡': 'deceased', '盲': 'blind', '妄': 'delusions', '荒': 'lays waste', '望': 'ambitions', '方': 'direction', '妨': 'disturb', '坊': 'boy', '芳': 'perfume', '肪': 'obese', '訪': 'call on', '放': 'release', '激': 'violence', '脱': 'undress', '説': 'rumors', '鋭': 'pointed', '曽': 'formerly', '増': 'increase', '贈': 'present', '東': 'east', '棟': 'ridgepoles', '凍': 'frozen', '妊': 'pregnancy', '廷': 'courts', '染': 'dye', '燃': 'burn', '賓': 'v.i.p.', '歳': 'age', '県': 'prefectures', '栃': 'horse-chestnuts', '地': 'ground', '池': 'pond', '虫': 'insect', '蛍': 'firefly', '蛇': 'snake', '虹': 'rainbows', '蝶': 'butterfly', '独': 'single', '蚕': 'silkworm', '風': 'wind', '己': 'self', '起': 'rouse', '妃': 'queen', '改': 'reform', '記': 'scribe', '包': 'wrapping', '胞': 'placenta', '砲': 'cannon', '泡': 'bubble', '亀': 'tortoise', '電': 'electric', '竜': 'dragon', '滝': 'waterfall', '豚': 'pork', '逐': 'pursue', '遂': 'attain', '家': 'house', '嫁': 'wife', '豪': 'strong', '腸': 'intestine', '場': 'location', '湯': 'hot water', '羊': 'sheep', '美': 'beauty', '洋': 'ocean', '詳': 'detailed', '鮮': 'fresh', '達': 'accomplishment', '羨': 'envious', '差': 'distinction', '着': 'donned', '唯': 'soloist', '焦': 'char', '礁': 'reef', '集': 'gather', '准': 'quasi', '進': 'advance', '雑': 'miscellaneous', '雌': 'feminine', '準': 'conform', '奮': 'stirred up', '奪': 'rob', '確': 'assurance', '午': 'noon', '許': 'permission', '歓': 'delight', '権': 'authority', '観': 'outlook', '羽': 'feathers', '習': 'learning', '翌': 'following', '曜': 'weekday', '濯': 'laundry', '曰': 'say', '困': 'quandary', '固': 'hardened', '国': 'country', '団': 'group', '因': 'cause', '姻': 'matrimony', '園': 'park', '回': 'times', '壇': 'podium', '店': 'store', '庫': 'warehouse', '庭': 'courtyard', '庁': 'government office', '床': 'bed', '麻': 'hemp', '磨': 'grind', '心': 'heart', '忘': 'forget', '忍': 'endure', '認': 'acknowledge', '忌': 'mourning', '志': 'intentions', '誌': 'document', '忠': 'loyalty', '串': 'shish-kebab', '患': 'affliction', '思': 'thinking', '恩': 'grace', '応': 'apply', '意': 'idea', '想': 'concept', '息': 'breathless', '憩': 'recess', '恵': 'favour', '恐': 'fear', '惑': 'beguiled', '感': 'emotions', '憂': 'melancholy', '寡': 'widow', '忙': 'busy', '悦': 'ecstasy', '恒': 'always', '悼': 'lament', '悟': 'enlightenment', '怖': 'dreadful', '慌': 'to panic', '悔': 'repents', '憎': 'hate', '慣': 'accustomed', '愉': 'pleasure', '惰': 'sloth', '慎': 'humility', '憾': 'remorse', '憶': 'recollection', '慕': 'yearn', '添': 'annexed', '必': 'invariably', '泌': 'ooze', '手': 'hand', '看': 'watches over', '摩': 'chafes', '我': 'ego', '義': 'righteousness', '議': 'deliberations', '犠': 'sacrifice', '抹': 'rubbing', '抱': 'embrace', '搭': 'board', '抄': 'extract', '抗': 'confronts', '批': 'criticized', '招': 'beckons', '拓': 'clear the land', '拍': 'clap', '打': 'strike', '拘': 'arrest', '捨': 'discard', '拐': 'kidnap', '摘': 'pinch', '挑': 'challenge', '指': 'finger', '持': 'hold', '括': 'fasten', '揮': 'brandish', '推': 'conjecture', '揚': 'hoisted', '提': 'proposal', '拳': 'fist', '損': 'damaged', '拾': 'pick-up', '担': 'shouldering', '拠': 'foothold', '描': 'sketch', '操': 'maneuver', '接': 'touched', '掲': 'postings', '掛': 'hang', '研': 'polished', '戒': 'commandments', '械': 'contraption', '鼻': 'nose', '刑': 'punishment', '型': 'molded', '才': 'genius', '財': 'property', '材': 'lumber', '存': 'retain', '在': 'exist', '乃': 'from', '携': 'portable', '及': 'reaches out', '吸': 'sucking', '扱': 'handle', '丈': 'length', '史': 'history', '吏': 'officer', '更': 'grow late', '硬': 'stiff', '又': 'again', '双': 'pair', '桑': 'mulberry', '隻': 'vessel', '護': 'safeguard', '獲': 'seized', '奴': 'guys', '怒': 'angry', '友': 'friend', '抜': 'slip out', '投': 'throw', '没': 'drown', '設': 'establishment', '撃': 'beating', '殻': 'husks', '支': 'branch', '技': 'skill', '枝': 'bough', '肢': 'limb', '茎': 'stalk', '怪': 'suspicious', '軽': 'light', '叔': 'uncle', '督': 'coach', '寂': 'loneliness', '淑': 'graceful', '反': 'anti', '坂': 'slope', '板': 'plank', '返': 'returns', '販': 'marketing', '爪': 'claw', '妥': 'gentle', '乳': 'milk', '浮': 'float', '将': 'leader', '奨': 'caution', '採': 'pick', '菜': 'vegetables', '受': 'accepts', '授': 'to give', '愛': 'love', '払': 'pay', '広': 'wide', '拡': 'broaden', '鉱': 'mineral', '弁': 'valve', '雄': 'masculine', '台': 'pedestal', '怠': 'neglect', '治': 'reign', '始': 'commencement', '胎': 'womb', '窓': 'window', '去': 'gone', '法': 'method', '会': 'meeting', '至': 'climax', '室': 'room', '到': 'arrives', '致': 'do', '互': 'mutually', '棄': 'abandoned', '育': 'brought up', '撤': 'remove', '充': 'allot', '銃': 'gun', '硫': 'sulfur', '流': 'current', '允': 'license', '唆': 'tempt', '出': 'exit', '山': 'mountain', '拙': 'awkward', '岩': 'boulder', '炭': 'charcoal', '岐': 'branches off', '峠': 'mountain peak', '崩': 'crumble', '密': 'secrecy', '蜜': 'honey', '嵐': 'storm', '崎': 'small peninsula', '入': 'in', '込': 'crowded', '分': 'part', '貧': 'poverty', '頒': 'partitioned', '公': 'public', '松': 'pine tree', '翁': 'venerable old man', '訟': 'sued', '谷': 'valley', '浴': 'bathe', '容': 'container', '溶': 'melted', '欲': 'long', '裕': 'abundant', '鉛': 'lead', '沿': 'runs alongside', '賞': 'prize', '党': 'party', '堂': 'temple', '常': 'usually', '裳': 'skirt', '掌': 'manipulates', '皮': 'pelt', '波': 'wave', '婆': 'old woman', '披': 'expose', '破': 'rends', '被': 'incur', '残': 'remainder', '殉': 'martyrdom', '殊': 'particularly', '殖': 'to enlarge', '列': 'file', '裂': 'splits', '烈': 'passionately', '死': 'death', '葬': 'burial', '瞬': 'winks', '耳': 'ear', '取': 'taking', '趣': 'gist', '最': 'utmost', '撮': 'snapshot', '恥': 'shame', '職': 'place of work', '聖': 'holy', '敢': 'daring', '聴': 'listener', '懐': 'breast', '慢': 'ridiculous', '漫': 'loose', '買': 'buy', '置': 'placement', '罰': 'penalty', '寧': 'rather', '濁': 'voice', '環': 'ring', '還': 'sent back', '夫': 'husband', '扶': 'aid', '渓': 'mountain stream', '規': 'standards', '替': 'exchanged', '賛': 'approve', '潜': 'submerge', '失': 'lost', '鉄': 'iron', '迭': 'transfer', '臣': 'retainer', '姫': 'princess', '蔵': 'storehouse', '臓': 'entrails', '賢': 'intelligent', '堅': 'strict', '臨': 'look to', '覧': 'read through', '巨': 'gigantic', '拒': 'repel', '力': 'power', '男': 'male', '労': 'labor', '募': 'recruited', '劣': 'inferiority', '功': 'achieve', '勧': 'persuading', '努': 'toiling', '励': 'encourage', '加': 'adds', '賀': 'congratulations', '架': 'erect', '脇': 'armpit', '脅': 'threaten', '協': 'co', '行': 'go', '律': 'rhythm', '復': 'restore', '得': 'gain', '従': 'accompany', '徒': 'junior', '待': 'wait', '往': 'journey', '征': 'subjugate', '径': 'diameter', '彼': 'he', '役': 'duty', '徳': 'benevolence', '徹': 'penetrate', '徴': 'indications', '懲': 'penal', '微': 'delicate', '街': 'boulevard', '衡': 'equilibrium', '稿': 'draft', '稼': 'earnings', '程': 'extent', '税': 'tax', '稚': 'immature', '和': 'harmony', '移': 'shift', '秒': 'second', '秋': 'autumn', '愁': 'distress', '私': 'private', '秩': 'regularity', '秘': 'secret', '称': 'appellations', '利': 'profits', '梨': 'pear tree', '穫': 'harvest', '穂': 'ear', '稲': 'rice plant', '香': 'incense', '季': 'seasons', '委': 'committee', '秀': 'excels', '透': 'transparent', '誘': 'entice', '穀': 'cereal', '菌': 'germs', '米': 'rice', '粉': 'flour', '粘': 'sticky', '粒': 'grain', '粧': 'cosmetics', '迷': 'astray', '粋': 'chic', '糧': 'provisions', '菊': 'chrysanthemum', '奥': 'heart', '数': 'number', '楼': 'watchtower', '類': 'sort', '漆': 'lacquer', '様': 'esq.', '求': 'requested', '球': 'ball', '救': 'salvation', '竹': 'bamboo', '笑': 'laugh', '笠': 'bamboo hat', '笹': 'bamboo grass', '筋': 'muscles', '箱': 'box', '筆': 'writing brush', '筒': 'cylinders', '等': 'etc.', '算': 'calculator', '答': 'solution', '策': 'scheme', '簿': 'registered', '築': 'fabrication', '人': 'person', '佐': 'assistant', '但': 'however', '住': 'dwells', '位': 'rank', '仲': 'go-between', '体': 'body', '悠': 'remote', '件': 'affair', '仕': 'attend', '他': 'other', '伏': 'prostrate', '伝': 'transmit', '仏': 'buddha', '休': 'rest', '仮': 'provisional', '伯': 'chief', '俗': 'vulgar', '信': 'faith', '佳': 'excellent', '依': 'reliable', '例': 'example', '個': 'individual', '健': 'healthy', '側': 'side', '侍': 'waiter', '停': 'halt', '値': 'price', '倣': 'emulated', '倒': 'overthrow', '偵': 'spy', '僧': 'buddhist priest', '億': 'hundred million', '儀': 'ceremonies', '償': 'reparation', '仙': 'hermit', '催': 'sponsor', '仁': 'humanity', '侮': 'scorn', '使': 'use', '便': 'convenience', '倍': 'double', '優': 'tenderness', '伐': 'downed', '宿': 'inn', '傷': 'wound', '保': 'protect', '褒': 'praise', '傑': 'greatness', '付': 'adhere', '符': 'tokens', '府': 'municipality', '任': 'responsibility', '賃': 'fare', '代': 'substitute', '袋': 'sack', '貸': 'lends', '化': 'change', '花': 'flower', '貨': 'freight', '傾': 'slanted', '何': 'what', '荷': 'baggage', '俊': 'keen', '傍': 'bystander', '久': 'long time', '畝': 'furrow', '囚': 'captured', '内': 'inside', '丙': 'third class', '柄': 'designs', '肉': 'meat', '腐': 'rotted', '座': 'sit', '卒': 'graduate', '傘': 'umbrella', '匁': 'monme', '以': 'by means of', '似': 'similar', '併': 'joining', '瓦': 'tile', '瓶': 'flower pot', '宮': 'shinto shrine', '営': 'occupation', '善': 'virtuous', '年': 'year', '夜': 'night', '液': 'fluid', '塚': 'mound', '幣': 'cash', '弊': 'abuse', '喚': 'yelling', '換': 'alternate', '融': 'dissolves', '施': 'alms', '旋': 'rotation', '遊': 'play', '旅': 'trip', '勿': 'not', '物': 'thing', '易': 'easy', '賜': 'grant', '尿': 'urine', '尼': 'nuns', '泥': 'mud', '塀': 'fence', '履': 'boots', '屋': 'roof', '握': 'grip', '屈': 'yield', '掘': 'digging', '堀': 'ditch', '居': 'reside', '据': 'set', '層': 'layer', '局': 'bureau', '遅': 'slow', '漏': 'leak', '刷': 'printing', '尺': 'shaku', '尽': 'exhaust', '沢': 'swamp', '訳': 'translated', '択': 'choose', '昼': 'daytime', '戸': 'door', '肩': 'shoulder', '房': 'tassel', '扇': 'fan', '炉': 'hearth', '戻': 'return', '涙': 'tears', '雇': 'employed', '顧': 'look back', '啓': 'discloses', '示': 'show', '礼': 'salute', '祥': 'fortunate', '祝': 'celebration', '福': 'blessing', '祉': 'welfare', '社': 'company', '視': 'inspecting', '奈': 'hell', '尉': 'military officer', '慰': 'consolation', '款': 'goodwill', '禁': 'prohibition', '襟': 'collar', '宗': 'religion', '崇': 'adoration', '祭': 'ritual', '察': 'guess', '擦': 'scrub', '由': 'reason', '抽': 'pluck', '油': 'oil', '袖': 'sleeves', '宙': 'mid-air', '届': 'delivers', '笛': 'flute', '軸': 'axis', '甲': 'armor', '押': 'push', '岬': 'small peninsula', '挿': 'insert', '申': 'speak', '伸': 'expands', '神': 'god', '捜': 'search', '果': 'fruit', '菓': 'candy', '課': 'chapters', '裸': 'naked', '斤': 'axe', '析': 'chopped', '所': 'place', '祈': 'pray', '近': 'near', '折': 'fold', '哲': 'philosophy', '逝': 'departed', '誓': 'vow', '暫': 'temporarily', '漸': 'steadily', '断': 'severance', '質': 'substance', '斥': 'rejected', '訴': 'accusation', '昨': 'yesterday', '詐': 'lie', '作': 'makes', '雪': 'snow', '録': 'record', '尋': 'interrogate', '急': 'hurries', '穏': 'calm', '侵': 'infringe', '浸': 'immerses', '寝': 'lie down', '婦': 'wife', '掃': 'sweeping', '当': 'hits', '争': 'contend', '浄': 'clean', '事': 'matter', '唐': "t'ang", '糖': 'sugar', '康': 'sane', '逮': 'apprehend', '伊': 'italy', '君': 'kun', '群': 'flock', '耐': 'proof', '需': 'demand', '儒': 'confucius', '端': 'edge', '両': 'both', '満': 'fill', '画': 'brush-stroke', '歯': 'teeth', '曲': 'bent', '曹': 'cadet', '遭': 'encounter', '漕': 'rowing', '槽': 'vat', '斗': 'measure', '料': 'fee', '科': 'department', '図': 'map', '用': 'utilized', '庸': 'comfortable', '備': 'equipment', '昔': 'once upon a time', '錯': 'confused', '借': 'borrow', '惜': 'pity', '措': 'set aside', '散': 'scatter', '廿': 'twenty', '庶': 'commoners', '遮': 'intercepted', '席': 'seat', '度': 'degrees', '渡': 'transit', '奔': 'bustles', '噴': 'erupts', '墳': 'tomb', '憤': 'aroused', '焼': 'baking', '暁': 'daybreak', '半': 'half', '伴': 'companion', '畔': 'paddy-ridge', '判': 'judgment', '券': 'ticket', '巻': 'scroll', '圏': 'spheres', '勝': 'victory', '藤': 'wisteria', '謄': 'mimeographed', '片': 'one-sided', '版': 'versions', '之': 'of', '乏': 'deprivation', '芝': 'turf', '不': 'negative', '否': 'negate', '杯': 'cupfuls', '矢': 'dart', '矯': 'rectify', '族': 'tribe', '知': 'knows', '智': 'wisdom', '矛': 'halberd', '柔': 'tender', '務': 'task', '霧': 'fog', '班': 'squad', '帰': 'homecoming', '弓': 'bow', '引': 'pulled', '弔': 'condolences', '弘': 'vast', '強': 'strongest', '弱': 'weaken', '沸': 'seething', '費': 'expense', '第': 'number', '弟': 'younger brother', '巧': 'ingenuity', '号': 'nickname', '朽': 'decays', '誇': 'boastful', '汚': 'dirty', '与': 'bestowed', '写': 'copy', '身': 'somebody', '射': 'shoot', '謝': 'apologizing', '老': 'old man', '考': 'considers', '孝': 'respect', '教': 'teach', '拷': 'torture', '者': 'someone', '煮': 'boiled', '著': 'renowned', '署': 'signature', '暑': 'hot', '諸': 'various', '猪': 'boar', '渚': 'shore', '賭': 'gambling', '峡': 'gorge', '狭': 'cramped', '挟': 'sandwiched', '追': 'chase', '師': 'expert', '帥': 'commander', '官': 'bureaucrat', '棺': 'coffin', '管': 'pipe', '父': 'father', '交': 'mingles', '効': 'merit', '較': 'contrast', '校': 'exam', '足': 'leg', '促': 'stimulated', '距': 'long-distance', '路': 'path', '露': 'dew', '跳': 'hop', '躍': 'leaps', '践': 'tread', '踏': 'steps', '骨': 'skeleton', '滑': 'slippery', '髄': 'marrow', '禍': 'calamity', '渦': 'whirlpool', '過': 'overdoing', '阪': 'heights', '阿': 'africa', '際': 'occasions', '障': 'hinder', '随': 'following', '陪': 'auxiliary', '陽': 'sunshine', '陳': 'line up', '防': 'warding off', '附': 'affixed', '院': 'institution', '陣': 'campground', '隊': 'regiment', '墜': 'crash', '降': 'descends', '階': 'storeys', '陛': 'highness', '隣': 'neighbours', '隔': 'isolate', '隠': 'concealed', '堕': 'degenerates', '陥': 'collapses', '穴': 'hole', '空': 'empty', '控': 'withdraw', '突': 'stabbed', '究': 'research', '窒': 'plugged up', '窃': 'stealth', '窪': 'depression', '搾': 'squeeze', '窯': 'kiln', '窮': 'cornered', '探': 'grope', '深': 'deep', '丘': 'hill', '岳': 'point', '兵': 'soldier', '浜': 'seacoast', '糸': 'thread', '織': 'woven', '繕': 'darn', '縮': 'shrinking', '繁': 'luxuriant', '縦': 'vertical', '線': 'line', '締': 'tightens', '維': 'fiber', '羅': 'gauze', '練': 'practice', '緒': 'thong', '続': 'continues', '絵': 'picture', '統': 'overall', '絞': 'strangling', '給': 'salary', '絡': 'entwines', '結': 'ties', '終': 'end', '級': 'class', '紀': 'chronicle', '紅': 'crimson', '納': 'settlement', '紡': 'spinning', '紛': 'distraction', '紹': 'introduction', '経': 'sutra', '紳': 'sire', '約': 'promise', '細': 'dainty', '累': 'accumulates', '索': 'cord', '総': 'general', '綿': 'cotton', '絹': 'silk', '繰': 'winding', '継': 'inherit', '緑': 'green', '縁': 'affinity', '網': 'netting', '緊': 'tense', '紫': 'purple', '縛': 'tie up', '縄': 'straw rope', '幼': 'Infancy', '後': 'behind', '幽': 'faint', '幾': 'how many', '機': 'mechanism', '玄': 'mystery', '畜': 'livestock', '蓄': 'amass', '弦': 'bow-string', '擁': 'hug', '滋': 'nourishing', '慈': 'mercy', '磁': 'magnetism', '系': 'lineage', '係': 'person in charge', '孫': 'grandchild', '懸': 'suspended', '却': 'instead', '脚': 'shins', '卸': 'wholesale', '御': 'honorable', '服': 'clothing', '命': 'fate', '令': 'orders', '零': 'zero', '齢': 'age', '冷': 'cool', '領': 'jurisdiction', '鈴': 'small bell', '勇': 'courage', '通': 'traffic', '踊': 'jump', '疑': 'doubts', '擬': 'mimic', '凝': 'congeals', '範': 'pattern', '犯': 'crime', '厄': 'unlucky', '危': 'dangerous', '宛': 'address', '腕': 'arm', '苑': 'garden', '怨': 'grudge', '柳': 'willow', '卵': 'egg', '留': 'detained', '貿': 'trade', '印': 'stamp', '興': 'entertain', '酉': 'sign of the bird', '酒': 'sake', '酌': 'bartender', '酵': 'fermentation', '酷': 'cruel', '酬': 'repay', '酪': 'dairy product', '酢': 'vinegar', '酔': 'drunk', '配': 'distributes', '酸': 'acid', '猶': 'furthermore', '尊': 'revered', '豆': 'beans', '頭': 'head', '短': 'short', '豊': 'bountiful', '鼓': 'drum', '喜': 'rejoice', '樹': 'timber-trees', '皿': 'dish', '血': 'blood', '盆': 'basin', '盟': 'alliance', '盗': 'steals', '温': 'warm', '監': 'overseer', '濫': 'overflow', '鑑': 'specimens', '猛': 'fierce', '盛': 'boom', '塩': 'salt', '銀': 'silver', '恨': 'regret', '根': 'roots', '即': 'instant', '爵': 'baron', '節': 'nodes', '退': 'retreat', '限': 'limit', '眼': 'eyeball', '良': 'good', '朗': 'melodious', '浪': 'wandering', '娘': 'daughter', '食': 'eats', '飯': 'meal', '飲': 'drink', '飢': 'hungry', '餓': 'starvation', '飾': 'decorator', '館': 'building', '養': 'foster', '飽': 'sated', '既': 'previously', '概': 'outline', '慨': 'rue', '平': 'evenly', '呼': 'calls', '坪': 'two-mat-area', '評': 'evaluate', '刈': 'reaped', '希': 'hope', '凶': 'villain', '胸': 'bosom', '離': 'detaching', '殺': 'killing', '純': 'genuine', '鈍': 'dull', '辛': 'spicy', '辞': 'resigns', '梓': 'catalpa', '宰': 'superintendent', '壁': 'wall', '避': 'evade', '新': 'new', '薪': 'fuel', '親': 'parent', '幸': 'happiness', '執': 'tenacity', '報': 'report', '叫': 'shout', '糾': 'twisted', '収': 'income', '卑': 'lowly', '碑': 'tombstone', '陸': 'land', '睦': 'intimate', '勢': 'forces', '熱': 'heat', '菱': 'diamonds', '陵': 'mausoleum', '亥': 'sign of the pig', '核': 'nucleus', '刻': 'engraves', '該': 'above-stated', '劾': 'censured', '述': 'mention', '術': 'art', '寒': 'cold', '醸': 'brew', '譲': 'delay', '壌': 'lot', '嬢': 'lass', '毒': 'poison', '素': 'elementary', '麦': 'barley', '青': 'blue', '精': 'refined', '請': 'solicit', '情': 'feelings', '晴': 'cleared-up', '清': 'pure', '静': 'quiet', '責': 'blame', '績': 'exploits', '積': 'volume', '債': 'bonds', '漬': 'pickling', '表': 'surface', '俵': 'bags', '潔': 'clean', '契': 'pledge', '喫': 'consume', '害': 'harm', '轄': 'control', '割': 'proportional', '憲': 'constitution', '生': 'life', '星': 'star', '姓': 'surname', '性': 'sex', '牲': 'animal sacrifice', '産': 'product', '隆': 'hump', '峰': 'summit', '縫': 'sew', '拝': 'worship', '寿': 'longevity', '鋳': 'casting', '籍': 'enroll', '春': 'spring', '椿': 'camellia', '泰': 'peace', '奏': 'playing music', '実': 'reality', '奉': 'dedication', '俸': 'salary', '棒': 'rod', '謹': 'discreet', '勤': 'diligently', '漢': 'sino', '嘆': 'sigh', '難': 'difficult', '華': 'flowers', '垂': 'drooping', '睡': 'drowsy', '錘': 'spindle', '乗': 'ride', '剰': 'surplus', '今': 'now', '含': 'included', '吟': 'recital', '念': 'wish', '琴': 'harp', '陰': 'shade', '予': 'beforehand', '序': 'preface', '預': 'deposit', '野': 'plains', '兼': 'concurrently', '嫌': 'dislikes', '鎌': 'sickle', '謙': 'modest', '廉': 'bargain', '西': 'west', '価': 'value', '要': 'need', '腰': 'loins', '票': 'ballot', '漂': 'drift', '標': 'signposts', '栗': 'chestnuts', '遷': 'transition', '覆': 'capsized', '煙': 'smoke', '南': 'south', '楠': 'camphor tree', '献': 'offering', '門': 'gate', '問': 'question', '閲': 'review', '閥': 'clique', '間': 'interval', '簡': 'simple', '開': 'open', '閉': 'closed', '閣': 'tower', '閑': 'leisure', '聞': 'hears', '潤': 'wet', '欄': 'column', '闘': 'fight', '倉': 'godown', '創': 'genesis', '非': 'mistake', '俳': 'haiku', '排': 'reject', '悲': 'sad', '罪': 'guilt', '輩': 'comrades', '扉': 'front door', '侯': 'lord', '候': 'climate', '決': 'decided', '快': 'cheerful', '偉': 'admirable', '違': 'difference', '緯': 'horizontal', '衛': 'defense', '韓': 'korea', '干': 'dry', '肝': 'liver', '刊': 'publishing', '汗': 'sweat', '軒': 'flats', '岸': 'beach', '幹': 'tree-trunk', '芋': 'potato', '宇': 'eaves', '余': 'too much', '除': 'excluded', '徐': 'gradually', '叙': 'described', '途': 'route', '斜': 'diagonal', '塗': 'paint', '束': 'bundle', '頼': 'trust', '瀬': 'rapids', '勅': 'imperial order', '疎': 'alienated', '速': 'quickly', '整': 'organizes', '剣': 'sabre', '険': 'steep', '検': 'examination', '倹': 'frugal', '重': 'heavy', '動': 'move', '勲': 'merit', '働': 'work', '種': 'species', '衝': 'collision', '薫': 'fragrant', '病': 'ill', '痴': 'stupid', '痘': 'pox', '症': 'symptoms', '疾': 'rapidly', '痢': 'diarrhea', '疲': 'exhausted', '疫': 'epidemic', '痛': 'pain', '癖': 'mannerism', '匿': 'hide', '匠': 'artisans', '医': 'doctor', '匹': 'equal', '区': 'ward', '枢': 'hinge', '殴': 'assault', '欧': 'europe', '抑': 're-presses', '仰': 'face-up', '迎': 'welcome', '登': 'ascends', '澄': 'lucidity', '発': 'discharged', '廃': 'abolish', '僚': 'colleague', '寮': 'dormitory', '療': 'healed', '彫': 'carving', '形': 'shape', '影': 'shadow', '杉': 'cedar trees', '彩': 'coloring', '彰': 'patent', '彦': 'lad', '顔': 'face', '須': 'ought', '膨': 'swells', '参': 'visit', '惨': 'wretched', '修': 'discipline', '珍': 'rare', '診': 'check-up', '文': 'sentence', '対': 'versus', '紋': 'family crest', '蚊': 'mosquito', '斉': 'adjusted', '剤': 'dose', '済': 'finish', '斎': 'purification', '粛': 'solemn', '塁': 'bases', '楽': 'music', '薬': 'medicine', '率': 'ratio', '渋': 'constrictive', '摂': 'surrogate', '央': 'center', '英': 'england', '映': 'reflects', '赤': 'red', '赦': 'pardon', '変': 'unusual', '跡': 'tracks', '蛮': 'barbarian', '恋': 'romance', '湾': 'gulf', '黄': 'yellow', '横': 'sideways', '把': 'grasp', '色': 'colours', '絶': 'discontinued', '艶': 'glossy', '肥': 'fertilizes', '甘': 'sweets', '紺': 'navy blue', '某': 'so & so', '謀': 'conspiracy', '媒': 'mediator', '欺': 'deceit', '棋': 'chess pieces', '旗': 'national flag', '期': 'period', '碁': 'go', '基': 'fundamentals', '甚': 'tremendously', '勘': 'intuition', '堪': 'withstand', '貴': 'precious', '遺': 'bequeathed', '遣': 'dispatch', '舞': 'dance', '無': 'nothingness', '組': 'association', '粗': 'coarse', '租': 'tariff', '祖': 'ancestors', '阻': 'thwart', '査': 'investigated', '助': 'help', '宜': 'best regards', '畳': 'tatami mat', '並': 'row', '普': 'universal', '譜': 'musical score', '湿': 'daffodil', '顕': 'appear', '繊': 'slender', '霊': 'spirits', '業': 'business', '撲': 'slap', '僕': 'me', '共': 'togetherness', '供': 'submit', '異': 'uncommon', '翼': 'wing', '洪': 'flood', '港': 'harbor', '暴': 'outburst', '爆': 'bomb', '恭': 'respect', '選': 'election', '殿': 'mr', '井': 'well', '囲': 'surrounded', '耕': 'till', '亜': 'asia', '悪': 'bad', '円': 'circular yen', '角': 'angle', '触': 'contact', '解': 'unravel', '再': 'again', '講': 'lecture', '購': 'subscriptions', '構': 'posture', '溝': 'gutter', '論': 'arguments', '倫': 'ethics', '輪': 'wheel', '偏': 'partially', '遍': 'everywhere', '編': 'compilation', '冊': 'tome', '典': 'code', '氏': 'family name', '紙': 'paper', '婚': 'marriage', '低': 'lowers', '抵': 'resistance', '底': 'bottom', '民': 'people', '眠': 'sleep', '捕': 'catch', '浦': 'bay', '蒲': 'bullrush', '舗': 'shop', '補': 'supplement', '邸': 'residence', '郭': 'enclosure', '郡': 'county', '郊': 'outskirts', '部': 'section', '都': 'metropolis', '郵': 'mail', '邦': 'home country', '郷': 'home town', '響': 'echo', '郎': 'son', '廊': 'corridor', '盾': 'shield', '循': 'sequence', '派': 'faction', '脈': 'veins', '衆': 'masses', '逓': 'parcel post', '段': 'grade', '鍛': 'forging', '后': 'empress', '幻': 'phantasm', '司': 'director', '伺': 'pay respects', '詞': 'parts of speech', '飼': 'raise', '嗣': 'heir', '舟': 'boat', '舶': 'liner', '航': 'navigator', '般': 'carrier', '盤': 'tray', '搬': 'conveyor', '船': 'ship', '艦': 'warship', '艇': 'rowboat', '瓜': 'melon', '弧': 'arc', '孤': 'orphan', '繭': 'cocoon', '益': 'benefit', '暇': 'spare time', '敷': 'spread', '来': 'come', '気': 'spirit', '汽': 'vapor', '飛': 'fly', '沈': 'sinking', '妻': 'wife', '衰': 'decline', '衷': 'inside', '面': 'mask', '革': 'leather', '靴': 'shoes', '覇': 'leadership', '声': 'voice', '呉': 'given', '娯': 'recreation', '誤': 'mistake', '蒸': 'steam', '承': 'be informed', '函': 'bin', '極': 'pole', '牙': 'tusk', '芽': 'bud', '邪': 'wicked', '雅': 'gracious', '釈': 'explanation', '番': 'turn', '審': 'hearing', '翻': 'flip', '藩': 'clan', '毛': 'furry', '耗': 'decrease', '尾': 'tail', '宅': 'house', '託': 'request', '為': 'do', '偽': 'falsehood', '長': 'long', '張': 'lengthened', '帳': 'notebook', '脹': 'dilate', '髪': 'hair', '展': 'unfold', '喪': 'miss', '巣': 'nest', '単': 'simple', '戦': 'war', '禅': 'zen', '弾': 'bullets', '桜': 'cherry blossom tree', '獣': 'animal', '脳': 'brain', '悩': 'trouble', '厳': 'stern', '鎖': 'chain', '挙': 'raise', '誉': 'reputation', '猟': 'game-hunting', '鳥': 'bird', '鳴': 'chirp', '鶴': 'crane', '烏': 'crow', '蔦': 'vine', '鳩': 'pigeon', '鶏': 'chicken', '島': 'island', '暖': 'warmth', '媛': 'beautiful woman', '援': 'help', '緩': 'slacken', '属': 'belong', '嘱': 'entrusted', '偶': 'accidentally', '遇': 'Interviews', '愚': 'foolish', '隅': 'corner', '逆': 'inverted', '塑': 'model', '岡': 'mount', '鋼': 'steel', '綱': 'hawser', '剛': 'sturdy', '缶': 'containers', '陶': 'pottery', '揺': 'swing', '謡': 'reciting', '就': 'concerning', '懇': 'sociable', '墾': 'groundbreaking', '免': 'excuse', '逸': 'elude', '晩': 'nightfall', '勉': 'exertion', '象': 'elephant', '像': 'statue', '馬': 'horse', '駒': 'pony', '験': 'verification', '騎': 'equestrian', '駐': 'stop-over', '駆': 'drive', '駅': 'station', '騒': 'disturb', '駄': 'burdensome', '驚': 'wonder', '篤': 'fervent', '騰': 'inflated', '虎': 'tiger', '虜': 'captive', '膚': 'skin', '虚': 'void', '戯': 'frolic', '虞': 'uneasiness', '慮': 'conservatism', '劇': 'drama', '虐': 'tyrannizes', '鹿': 'deer'}

#JoyoKanji
ShouGaku1Nen = ["一", "右", "雨", "円", "王", "音", "下", "火", "花", "貝", "学", "気", "休", "玉", "金", "九", "空", "月", "犬", "見", "五", "口", "校", "左", "三", "山", "四", "子", "糸", "字", "耳", "七", "車", "手", "十", "出", "女", "小", "上", "森", "人", "水", "正", "生", "青", "石", "赤", "先", "千", "川", "早", "草", "足", "村", "大", "男", "竹", "中", "虫", "町", "天", "田", "土", "二", "日", "入", "年", "白", "八", "百", "文", "本", "名", "木", "目", "夕", "立", "力", "林", "六"]
ShouGaku2Nen = ["引", "羽", "雲", "園", "遠", "黄", "何", "夏", "家", "科", "歌", "画", "会", "回", "海", "絵", "外", "角", "楽", "活", "間", "丸", "岩", "顔", "帰", "汽", "記", "弓", "牛", "魚", "京", "強", "教", "近", "兄", "形", "計", "元", "原", "言", "古", "戸", "午", "後", "語", "交", "光", "公", "工", "広", "考", "行", "高", "合", "国", "黒", "今", "才", "細", "作", "算", "姉", "市", "思", "止", "紙", "寺", "時", "自", "室", "社", "弱", "首", "秋", "週", "春", "書", "少", "場", "色", "食", "心", "新", "親", "図", "数", "星", "晴", "声", "西", "切", "雪", "線", "船", "前", "組", "走", "多", "太", "体", "台", "谷", "知", "地", "池", "茶", "昼", "朝", "長", "鳥", "直", "通", "弟", "店", "点", "電", "冬", "刀", "東", "当", "答", "頭", "同", "道", "読", "内", "南", "肉", "馬", "買", "売", "麦", "半", "番", "父", "風", "分", "聞", "米", "歩", "母", "方", "北", "妹", "毎", "万", "明", "鳴", "毛", "門", "夜", "野", "矢", "友", "曜", "用", "来", "理", "里", "話"]
ShouGaku3Nen = ["悪", "安", "暗", "委", "意", "医", "育", "員", "飲", "院", "運", "泳", "駅", "横", "屋", "温", "化", "荷", "界", "開", "階", "寒", "感", "漢", "館", "岸", "期", "起", "客", "宮", "急", "球", "究", "級", "去", "橋", "業", "局", "曲", "銀", "区", "苦", "具", "君", "係", "軽", "決", "血", "研", "県", "庫", "湖", "向", "幸", "港", "号", "根", "祭", "坂", "皿", "仕", "使", "始", "指", "死", "詩", "歯", "事", "持", "次", "式", "実", "写", "者", "主", "取", "守", "酒", "受", "州", "拾", "終", "習", "集", "住", "重", "宿", "所", "暑", "助", "勝", "商", "昭", "消", "章", "乗", "植", "深", "申", "真", "神", "身", "進", "世", "整", "昔", "全", "想", "相", "送", "息", "速", "族", "他", "打", "対", "待", "代", "第", "題", "炭", "短", "談", "着", "柱", "注", "丁", "帳", "調", "追", "定", "庭", "笛", "鉄", "転", "登", "都", "度", "島", "投", "湯", "等", "豆", "動", "童", "農", "波", "配", "倍", "箱", "畑", "発", "反", "板", "悲", "皮", "美", "鼻", "筆", "氷", "表", "病", "秒", "品", "夫", "負", "部", "服", "福", "物", "平", "返", "勉", "放", "味", "命", "面", "問", "役", "薬", "油", "有", "由", "遊", "予", "様", "洋", "羊", "葉", "陽", "落", "流", "旅", "両", "緑", "礼", "列", "練", "路", "和"]
ShouGaku4Nen = ["愛", "案", "以", "位", "囲", "胃", "衣", "印", "栄", "英", "塩", "央", "億", "加", "果", "課", "貨", "芽", "改", "械", "害", "街", "各", "覚", "完", "官", "管", "観", "関", "願", "喜", "器", "希", "旗", "機", "季", "紀", "議", "救", "求", "泣", "給", "挙", "漁", "競", "共", "協", "鏡", "極", "訓", "軍", "郡", "型", "径", "景", "芸", "欠", "結", "健", "建", "験", "固", "候", "功", "好", "康", "航", "告", "差", "最", "菜", "材", "昨", "刷", "察", "札", "殺", "参", "散", "産", "残", "司", "史", "士", "氏", "試", "児", "治", "辞", "失", "借", "種", "周", "祝", "順", "初", "唱", "松", "焼", "照", "省", "笑", "象", "賞", "信", "臣", "成", "清", "静", "席", "積", "折", "節", "説", "戦", "浅", "選", "然", "倉", "巣", "争", "側", "束", "続", "卒", "孫", "帯", "隊", "達", "単", "置", "仲", "貯", "兆", "腸", "低", "停", "底", "的", "典", "伝", "徒", "努", "灯", "働", "堂", "得", "特", "毒", "熱", "念", "敗", "梅", "博", "飯", "費", "飛", "必", "標", "票", "不", "付", "府", "副", "粉", "兵", "別", "変", "辺", "便", "包", "法", "望", "牧", "末", "満", "未", "脈", "民", "無", "約", "勇", "要", "養", "浴", "利", "陸", "料", "良", "量", "輪", "類", "令", "例", "冷", "歴", "連", "労", "老", "録"]
ShouGaku5Nen = ["圧", "易", "移", "因", "営", "永", "衛", "液", "益", "演", "往", "応", "恩", "仮", "価", "可", "河", "過", "賀", "解", "快", "格", "確", "額", "刊", "幹", "慣", "眼", "基", "寄", "規", "技", "義", "逆", "久", "旧", "居", "許", "境", "興", "均", "禁", "句", "群", "経", "潔", "件", "券", "検", "険", "減", "現", "限", "個", "故", "護", "効", "厚", "構", "耕", "講", "鉱", "混", "査", "再", "妻", "採", "災", "際", "在", "罪", "財", "桜", "雑", "賛", "酸", "師", "志", "支", "枝", "資", "飼", "似", "示", "識", "質", "舎", "謝", "授", "修", "術", "述", "準", "序", "承", "招", "証", "常", "情", "条", "状", "織", "職", "制", "勢", "性", "政", "精", "製", "税", "績", "責", "接", "設", "絶", "舌", "銭", "祖", "素", "総", "像", "増", "造", "則", "測", "属", "損", "態", "貸", "退", "団", "断", "築", "張", "提", "程", "敵", "適", "統", "導", "銅", "徳", "独", "任", "燃", "能", "破", "判", "版", "犯", "比", "肥", "非", "備", "俵", "評", "貧", "婦", "富", "布", "武", "復", "複", "仏", "編", "弁", "保", "墓", "報", "豊", "暴", "貿", "防", "務", "夢", "迷", "綿", "輸", "余", "預", "容", "率", "略", "留", "領"]
ShouGaku6Nen = ["異", "遺", "域", "宇", "映", "延", "沿", "我", "灰", "拡", "閣", "革", "割", "株", "巻", "干", "看", "簡", "危", "揮", "机", "貴", "疑", "吸", "供", "胸", "郷", "勤", "筋", "敬", "系", "警", "劇", "激", "穴", "憲", "権", "絹", "厳", "源", "呼", "己", "誤", "后", "孝", "皇", "紅", "鋼", "降", "刻", "穀", "骨", "困", "砂", "座", "済", "裁", "策", "冊", "蚕", "姿", "私", "至", "視", "詞", "誌", "磁", "射", "捨", "尺", "若", "樹", "収", "宗", "就", "衆", "従", "縦", "縮", "熟", "純", "処", "署", "諸", "除", "傷", "将", "障", "城", "蒸", "針", "仁", "垂", "推", "寸", "盛", "聖", "誠", "宣", "専", "泉", "洗", "染", "善", "創", "奏", "層", "操", "窓", "装", "臓", "蔵", "存", "尊", "宅", "担", "探", "誕", "暖", "段", "値", "宙", "忠", "著", "庁", "潮", "頂", "賃", "痛", "展", "党", "糖", "討", "届", "難", "乳", "認", "納", "脳", "派", "俳", "拝", "背", "肺", "班", "晩", "否", "批", "秘", "腹", "奮", "並", "閉", "陛", "片", "補", "暮", "宝", "訪", "亡", "忘", "棒", "枚", "幕", "密", "盟", "模", "訳", "優", "郵", "幼", "欲", "翌", "乱", "卵", "覧", "裏", "律", "臨", "朗", "論"]

ChuuGaku1Nen = ["亜", "哀", "握", "扱", "依", "偉", "威", "尉", "慰", "為", "維", "緯", "違", "井", "壱", "逸", "稲", "芋", "姻", "陰", "隠", "韻", "渦", "浦", "影", "詠", "鋭", "疫", "悦", "謁", "越", "閲", "宴", "援", "炎", "煙", "猿", "縁", "鉛", "汚", "凹", "奥", "押", "欧", "殴", "翁", "沖", "憶", "乙", "卸", "穏", "佳", "嫁", "寡", "暇", "架", "禍", "稼", "箇", "華", "菓", "蚊", "雅", "餓", "介", "塊", "壊", "怪", "悔", "懐", "戒", "拐", "皆", "劾", "慨", "概", "涯", "該", "垣", "嚇", "核", "殻", "獲", "穫", "較", "郭", "隔", "岳", "掛", "潟", "喝", "括", "渇", "滑", "褐", "轄", "且", "刈", "乾", "冠", "勘", "勧", "喚", "堪", "寛", "患", "憾", "換", "敢", "棺", "款", "歓", "汗", "環", "甘", "監", "緩", "缶", "肝", "艦", "貫", "還", "鑑", "閑", "陥", "含", "頑", "企", "奇", "岐", "幾", "忌", "既", "棋", "棄", "祈", "軌", "輝", "飢", "騎", "鬼", "偽", "儀", "宜", "戯", "擬", "欺", "犠", "菊", "吉", "喫", "詰", "却", "脚", "虐", "丘", "及", "朽", "窮", "糾", "巨", "拒", "拠", "虚", "距", "享", "凶", "叫", "峡", "恐", "恭", "挟", "況", "狂", "狭", "矯", "脅", "響", "驚", "仰", "凝", "暁", "斤", "琴", "緊", "菌", "襟", "謹", "吟", "駆", "愚", "虞", "偶", "遇", "隅", "屈", "掘", "靴", "繰", "桑", "勲", "薫", "傾", "刑", "啓", "契", "恵", "慶", "憩", "掲", "携", "渓", "継", "茎", "蛍", "鶏", "迎", "鯨", "撃", "傑", "倹", "兼", "剣", "圏", "堅", "嫌", "懸", "献", "肩", "謙", "賢", "軒", "遣", "顕", "幻", "弦", "玄", "孤", "弧", "枯", "誇", "雇", "顧", "鼓", "互", "呉", "娯", "御", "悟", "碁", "侯", "坑", "孔", "巧", "恒", "慌", "抗", "拘", "控", "攻", "更", "江", "洪", "溝", "甲", "硬", "稿", "絞", "綱", "肯", "荒", "衡", "貢", "購", "郊", "酵", "項", "香", "剛", "拷", "豪", "克", "酷", "獄", "腰", "込", "墾", "婚", "恨", "懇", "昆", "紺", "魂", "佐", "唆", "詐", "鎖", "債", "催", "宰", "彩", "栽", "歳", "砕", "斎", "載", "剤", "咲", "崎", "削", "搾", "索", "錯"]
ChuuGaku2Nen = ["撮", "擦", "傘", "惨", "桟", "暫", "伺", "刺", "嗣", "施", "旨", "祉", "紫", "肢", "脂", "諮", "賜", "雌", "侍", "慈", "滋", "璽", "軸", "執", "湿", "漆", "疾", "芝", "赦", "斜", "煮", "遮", "蛇", "邪", "勺", "爵", "酌", "釈", "寂", "朱", "殊", "狩", "珠", "趣", "儒", "寿", "需", "囚", "愁", "秀", "臭", "舟", "襲", "酬", "醜", "充", "柔", "汁", "渋", "獣", "銃", "叔", "淑", "粛", "塾", "俊", "瞬", "准", "循", "旬", "殉", "潤", "盾", "巡", "遵", "庶", "緒", "叙", "徐", "償", "匠", "升", "召", "奨", "宵", "尚", "床", "彰", "抄", "掌", "昇", "晶", "沼", "渉", "焦", "症", "硝", "礁", "祥", "称", "粧", "紹", "肖", "衝", "訟", "詔", "詳", "鐘", "丈", "冗", "剰", "壌", "嬢", "浄", "畳", "譲", "醸", "錠", "嘱", "飾", "殖", "触", "辱", "伸", "侵", "唇", "娠", "寝", "審", "慎", "振", "浸", "紳", "薪", "診", "辛", "震", "刃", "尋", "甚", "尽", "迅", "陣", "酢", "吹", "帥", "炊", "睡", "粋", "衰", "遂", "酔", "錘", "随", "髄", "崇", "枢", "据", "杉", "澄", "瀬", "畝", "是", "姓", "征", "牲", "誓", "請", "逝", "斉", "隻", "惜", "斥", "析", "籍", "跡", "拙", "摂", "窃", "仙", "占", "扇", "栓", "潜", "旋", "繊", "薦", "践", "遷", "銑", "鮮", "漸", "禅", "繕", "塑", "措", "疎", "礎", "租", "粗", "訴", "阻", "僧", "双", "喪", "壮", "捜", "掃", "挿", "曹", "槽", "燥", "荘", "葬", "藻", "遭", "霜", "騒", "憎", "贈", "促", "即", "俗", "賊", "堕", "妥", "惰", "駄", "耐", "怠", "替", "泰", "滞", "胎", "袋", "逮", "滝", "卓", "択", "拓", "沢", "濯", "託", "濁", "諾", "但", "奪", "脱", "棚", "丹", "嘆", "淡", "端", "胆", "鍛", "壇", "弾", "恥", "痴", "稚", "致", "遅", "畜", "蓄", "逐", "秩", "窒", "嫡", "抽", "衷", "鋳", "駐", "弔", "彫", "徴", "懲", "挑", "眺", "聴", "脹", "超", "跳", "勅", "朕", "沈", "珍", "鎮", "陳", "津", "墜", "塚", "漬", "坪", "釣", "亭", "偵", "貞", "呈", "堤", "帝", "廷", "抵", "締", "艇", "訂", "逓", "邸", "泥", "摘", "滴", "哲", "徹", "撤"]
ChuuGaku3Nen = ["迭", "添", "殿", "吐", "塗", "斗", "渡", "途", "奴", "怒", "倒", "凍", "唐", "塔", "悼", "搭", "桃", "棟", "盗", "痘", "筒", "到", "謄", "踏", "逃", "透", "陶", "騰", "闘", "洞", "胴", "峠", "匿", "督", "篤", "凸", "突", "屯", "豚", "曇", "鈍", "縄", "軟", "尼", "弐", "如", "尿", "妊", "忍", "寧", "猫", "粘", "悩", "濃", "把", "覇", "婆", "廃", "排", "杯", "輩", "培", "媒", "賠", "陪", "伯", "拍", "泊", "舶", "薄", "迫", "漠", "爆", "縛", "肌", "鉢", "髪", "伐", "罰", "抜", "閥", "伴", "帆", "搬", "畔", "繁", "般", "藩", "販", "範", "煩", "頒", "盤", "蛮", "卑", "妃", "彼", "扉", "披", "泌", "疲", "碑", "罷", "被", "避", "尾", "微", "匹", "姫", "漂", "描", "苗", "浜", "賓", "頻", "敏", "瓶", "怖", "扶", "敷", "普", "浮", "符", "腐", "膚", "譜", "賦", "赴", "附", "侮", "舞", "封", "伏", "幅", "覆", "払", "沸", "噴", "墳", "憤", "紛", "雰", "丙", "併", "塀", "幣", "弊", "柄", "壁", "癖", "偏", "遍", "舗", "捕", "穂", "募", "慕", "簿", "倣", "俸", "奉", "峰", "崩", "抱", "泡", "砲", "縫", "胞", "芳", "褒", "邦", "飽", "乏", "傍", "剖", "坊", "妨", "帽", "忙", "房", "某", "冒", "紡", "肪", "膨", "謀", "僕", "墨", "撲", "朴", "没", "堀", "奔", "翻", "凡", "盆", "摩", "磨", "魔", "麻", "埋", "膜", "又", "抹", "繭", "慢", "漫", "魅", "岬", "妙", "眠", "矛", "霧", "婿", "娘", "銘", "滅", "免", "茂", "妄", "猛", "盲", "網", "耗", "黙", "戻", "紋", "匁", "厄", "躍", "柳", "愉", "癒", "諭", "唯", "幽", "悠", "憂", "猶", "裕", "誘", "雄", "融", "与", "誉", "庸", "揚", "揺", "擁", "溶", "窯", "謡", "踊", "抑", "翼", "羅", "裸", "頼", "雷", "絡", "酪", "欄", "濫", "吏", "履", "痢", "離", "硫", "粒", "隆", "竜", "慮", "虜", "了", "僚", "寮", "涼", "猟", "療", "糧", "陵", "倫", "厘", "隣", "塁", "涙", "累", "励", "鈴", "隷", "零", "霊", "麗", "齢", "暦", "劣", "烈", "裂", "廉", "恋", "錬", "炉", "露", "廊", "楼", "浪", "漏", "郎", "賄", "惑", "枠", "湾", "腕"]

Added2010 = ["藤", "誰", "俺", "岡", "頃", "奈", "阪", "韓", "弥", "那", "鹿", "斬", "虎", "狙", "脇", "熊", "尻", "旦", "闇", "篭", "呂", "亀", "頬", "膝", "鶴", "匂", "沙", "須", "椅", "股", "眉", "挨", "拶", "鎌", "凄", "喉", "拭", "貌", "塞", "蹴", "鍵", "膳", "袖", "潰", "謎", "駒", "剥", "稽", "鍋", "湧", "葛", "梨", "曽", "賭", "貼", "拉", "枕", "顎", "苛", "蓋", "裾", "腫", "爪", "嵐", "鬱", "妖", "藍", "捉", "宛", "崖", "叱", "瓦", "拳", "乞", "呪", "汰", "勃", "昧", "唾", "艶", "痕", "諦", "餅", "瞳", "椎", "唄", "隙", "淫", "錦", "箸", "戚", "妬", "釜", "蔑", "嗅", "蜜", "戴", "痩", "怨", "醒", "詣", "窟", "巾", "蜂", "骸", "弄", "嫉", "罵", "璧", "阜", "埼", "伎", "曖", "餌", "爽", "詮", "柿", "芯", "綻", "肘", "麓", "憧", "頓", "牙", "咽", "嘲", "臆", "挫", "溺", "侶", "丼", "瘍", "僅", "柵", "睦", "腎", "梗", "瑠", "羨", "酎", "畿", "畏", "瞭", "踪", "栃", "蔽", "茨", "慄", "傲", "虹", "捻", "臼", "喩", "萎", "腺", "桁", "玩", "冶", "羞", "惧", "遡", "舷", "貪", "刹", "采", "堆", "煎", "斑", "冥", "遜", "旺", "勾", "麺", "璃", "串", "塡", "箋", "脊", "緻", "辣", "摯", "汎", "毀", "賂", "氾", "諧", "媛", "哺", "彙", "恣", "沃", "憬", "捗", "訃", "楷", "錮"]
AllKanji = ShouGaku1Nen + ShouGaku2Nen + ShouGaku3Nen + ShouGaku4Nen + ShouGaku5Nen + ShouGaku6Nen + ChuuGaku1Nen + ChuuGaku2Nen + ChuuGaku3Nen

kanjiList = [""]

def Font(font, fontSize, fontWeight, fontSlant):
        font_ = f"{font} {fontSize} {fontWeight} {fontSlant}"
        return font_
        
def destroy(widget, type = "place"):
    if type == "place":
        widget.place_forget()
    elif type == "pack":
        widget.pack_forget()

class Graphics(object):
    """docstring for Graphics"""
    def __init__(self, xSize, ySize):
        super(Graphics, self).__init__()
        self.ShouGaku1Nen = ShouGaku1Nen
        self.ShouGaku2Nen = ShouGaku2Nen
        self.ShouGaku3Nen = ShouGaku3Nen
        self.ShouGaku4Nen = ShouGaku4Nen
        self.ShouGaku5Nen = ShouGaku5Nen
        self.ShouGaku6Nen = ShouGaku6Nen
        self.ChuuGaku1Nen = ChuuGaku1Nen
        self.ChuuGaku2Nen = ChuuGaku2Nen
        self.ChuuGaku3Nen = ChuuGaku3Nen
        self.Added2010 = Added2010

        self.xSize = xSize
        self.ySize = ySize

        self.scene = "menu"
        self.subScene = ""

        self.getKanjisCount = 0
        self.dailyKanjisCount = 0
        self.kanjiFocusCount = 0
        self.createankiCount = 0

        #Create interface
        self.WINDOW()

    #Get libreoffice calc spreadsheet
    def WriteCalc(self, filename, kanjis, meanings, readings, exampleWords, examplesReadings, exampleMeanings):
        
        for i in self.languageButtons:
            destroy(i)
        for i in self.entryTittles:
            destroy(i)
        for i in self.kanjisEntry:
            destroy(i)

        kanjis = kanjis.strip("\n")

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        e = 1
        for i in kanjis:
            ws.cell(row = e, column = 1, value = i)
            e += 1 

        e = 1
        for i in meanings:
            ws.cell(row = e, column = 2, value = i[0])
            e += 1 
        
        e = 1
        for i in readings:
            ws.cell(row = e, column = 3, value = i[0])
            ws.cell(row = e, column = 4, value = i[1])
            e += 1
        
        a = 5
        e = 1
        for i in range(len(kanjis)):
            o = 0
            a = 5
            for word in exampleWords[i]:
                ws.cell(row = e, column = a, value = word)
                ws.cell(row = e, column = a + 1, value = examplesReadings[i][o])
                #print(exampleMeanings)
                ws.cell(row = e, column = a + 2, value = exampleMeanings[i][o])

                a += 3
                o += 1
            e += 1


        font = Font("none", "30", "bold", "roman")

        self.entryTittles[0].place(x = 300, y = 300, anchor = "center")
        self.entryTittles[0].configure(text = "Finished!", font = font) 

        wb.save(f"{filename}.xlsx")

        df = pd.read_excel(f"{filename}.xlsx")
        df.to_csv(f"{filename}.csv", sep = ",", quoting = 1, encoding = "utf8", index = False)

        print("finished")


    #Search Kanjis on internet for study
    def SearchKanjis(self, language, kanjis):
        result = []
        japaneseOnlineURL = f"http://japonesonline.com/kanjis/busqueda/?s={kanjis}&x=0&y=0" if language == "es" else f"https://www.kanshudo.com/search?q={kanjis}"
        webbrowser.open(japaneseOnlineURL, autoraise=False)

        font = Font("none", "20", "bold", "roman")
        
        if language == "en":
            self.heisigLabels.append(tkinter.Label(self.window, text = "Heisig meanings", height = 1, width = 20, bg = "#f2f2f4", fg = "#2c2c2c", font = font))
        elif language == "es":
            self.heisigLabels.append(tkinter.Label(self.window, text = "Significados Heisig", height = 1, width = 20, bg = "#f2f2f4", fg = "#2c2c2c", font = font))

        self.heisigLabels[0].place(x = 300, y = 100, anchor = "center")

        for i in self.languageButtons:
            destroy(i)

        x = 200
        y = 170
        font = Font("none", "15", "normal", "roman")

        count = 1
        for kanji in kanjis:
            basicJapaneseURL = "https://japonesbasico.com/kanji/" + f"{kanji}" if language == "es" else f"https://jisho.org/search/{kanji}"

            #webbrowser.open(basicJapaneseURL)

            try:
                if language == "es":
                    self.heisigLabels.append(tkinter.Label(self.window, text = f"{kanji}: {(HeisigEs[kanji]).capitalize()}", height = 1, bg = "#f2f2f4", fg = "#2c2c2c", font = font))
                elif language == "en":
                    self.heisigLabels.append(tkinter.Label(self.window, text = f"{kanji}: {(HeisigEn[kanji]).capitalize()}", bg = "#f2f2f4", fg = "#2c2c2c", font = font))
                self.heisigLabels[count].place(x = x, y = y)

            except:
                if language == "es":
                    self.heisigLabels.append(tkinter.Label(self.window, text = f"{kanji}: no encontrado", height = 1, bg = "#f2f2f4", fg = "#2c2c2c", font = font))
                elif language == "en":
                    self.heisigLabels.append(tkinter.Label(self.window, text = f"{kanji}: not found", height = 1, bg = "#f2f2f4", fg = "#2c2c2c", font = font))
                self.heisigLabels[count].place(x = x, y = y)

            y += 50
            count += 1

    def ERROR(self):
        self.Manager("show", "menu")

        font = Font("none", "30", "bold", "roman")
        self.Error = tkinter.Label(self.window, text = "ERROR\nDoesn't supported yet", bg = "#f2f2f4", fg = "#2c2c2c", font = font)
        self.Error.place(x = 300, y = 300, anchor = "center")

        self.window.after(3000, self.Error.place_forget)

    def DaillyKanjisCommand(self):
        #Create Label
        font = Font("none", "25", "bold", "roman")

        self.kanjisLabel = tkinter.Label(self.window, text = DailyKanji(GetDate()), height = 1, width = 20, bg = "#f2f2f4", fg = "#2c2c2c", font = font)
        self.kanjisLabel.place(x = 300, y = 50, anchor = "center")

        self.heisigLabels = []

        self.tittle.place_forget()

        font = Font("none", "20", "bold", "roman")

        self.languageButtons = []
        
        x = 200
        y = 100

        e = 0
        for i in ["en", "es"]:
            self.languageButtons.append(tkinter.Button(self.window, text = i.capitalize(), bg = "#ffffff", fg = "#2c2c2c",bd = "3", highlightcolor = "#f5f5f5", font = font, command= lambda i=i: self.SearchKanjis(i, DailyKanji(GetDate()))))
            self.languageButtons[e].place(x = x, y = y, anchor = "nw")

            x += 100
            e += 1
        self.dailyKanjisCount += 1

        self.Manager("hide", "menu")
        self.scene = "dailyKanjis"

    def CreateAnkiDeckCommand(self):
        #kanjis = input("Enter the kanjis of that you wanna create the deck: ") if language == "es" else print("error")

        #Create Label
        font = Font("none", "25", "bold", "roman")

        self.ankiTittle = tkinter.Label(self.window, text = "Create Anki deck", height = 1, width = 20, bg = "#f2f2f4", fg = "#2c2c2c", font = font)
        self.ankiTittle.place(x = 300, y = 50, anchor = "center")
        self.tittle.place_forget()

        #Create entries
        #

        x = 300
        y = 250
        width = 30
        height = 5

        self.kanjisEntry = []
        self.entryTittles = []

        font = Font("none", "15", "normal", "roman")
        
        e = 0
        for i in ["Enter the kanjis for create the deck", "Enter the file name"]:
            self.entryTittles.append(tkinter.Label(self.window, text = i, height = 1, bg = "#f2f2f4", fg = "#2c2c2c", font = font))
            self.entryTittles[e].place(x = x, y = y - 40, anchor = "center")

            self.kanjisEntry.append(tkinter.Text(self.window, bg = "#ffffff", width = width, height = height))
            self.kanjisEntry[e].place(x = x, y = y, anchor = "n")

            y += 160
            width -= 5
            height -= 3
            e += 1


        self.languageButtons = []


        font = Font("none", "15", "normal", "roman")
        self.languageInstructions = tkinter.Label(self.window, text = "Click a button to enter", height = 1, bg = "#f2f2f4", fg = "#2c2c2c", font = font)
        self.languageInstructions.place(x = 300, y = 85, anchor = "center")

        font = Font("none", "20", "bold", "roman")      
        x = 200
        y = 100
        e = 0
        for i in ["en", "es"]:
            if i == "en":
                self.languageButtons.append(tkinter.Button(self.window, text = i.capitalize(), bg = "#ffffff", fg = "#2c2c2c",bd = "3", highlightcolor = "#f5f5f5", font = font, command= self.ERROR))#self.WriteCalc(self.kanjisEntry[1].get("1.0", "end"), self.kanjisEntry[0].get("1.0", "end"), kanji.GetKanjiMeaningsEn(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiReadingsEn(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiExpamplesEn(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiExampleReadingsEn(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiExampleMeaningEn(self.kanjisEntry[0].get("1.0", "end")))))
            elif i == "es":
                self.languageButtons.append(tkinter.Button(self.window, text = i.capitalize(), bg = "#ffffff", fg = "#2c2c2c",bd = "3", highlightcolor = "#f5f5f5", font = font, command= lambda: self.WriteCalc(self.kanjisEntry[1].get("1.0", "end"), self.kanjisEntry[0].get("1.0", "end"), kanji.GetKanjiMeaningsEs(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiReadingsEs(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiExpamplesEs(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiExampleReadingsEs(self.kanjisEntry[0].get("1.0", "end")), kanji.GetKanjiExampleMeaningEs(self.kanjisEntry[0].get("1.0", "end")))))

            self.languageButtons[e].place(x = x, y = y, anchor = "nw")

            x += 100
            e += 1
        
        self.createankiCount += 1

        self.Manager("hide", "menu")
        self.scene = "anki"

    def GetKanjisCommand(self):
        #Create text box
        #Create kanji grades buttons
        x = 100
        y = 80
        xDelta = 70
        yDelta = 150

        font = Font("none", "15", "normal", "roman")

        self.gradesButtons = []
        #grades = ["１年", "小学２年", "小学３年", "小学４年", "小学５年", "小学６年", "中学１年", "中学２年", "中学３年", "２０１０年の改定"]

        e = 0
        a = 0

        box = [(x, y, "nw"), (x + xDelta, y, "nw"), (x + xDelta * 2, y, "nw"), (x + xDelta * 3, y, "nw"), (x + xDelta * 4, y, "nw"), (x + xDelta * 5, y, "nw"),
            (x +  xDelta, y + yDelta, "center"), (x + xDelta * 2.5, y + yDelta, "center"), (x + xDelta * 4, y + yDelta, "center"),
             (x + xDelta, y + yDelta * 1.7, "nw")]

        anchor = "nw"

        for i in ["1", "2", "3", "4", "5", "6", "Int 1", "Int 2", "Int 3", "Added in 2010"]:
            self.gradesButtons.append(tkinter.Button(self.window, text = i, bg = "#ffffff", height = 1, fg = "#2c2c2c",bd = "3", highlightcolor = "#f5f5f5", font = font, command=  lambda i=i: self.KanjiGrade(i)))
            self.gradesButtons[a].place(x = box[a][0], y = box[a][1], anchor = box[a][2])

            a += 1
            e += 50

        font = Font("none", "20", "bold", "roman")

        x = 270
        y = 50

        box = [(x, y), (x, y * 3.5), (x, y * 6)]

        e = 0
        self.gradesTittles = []
        for i in ["Primary", "Intermediate", "Extra"]:
            self.gradesTittles.append(tkinter.Label(self.window, text = i, height = 1, bg = "#f2f2f4", fg = "#2c2c2c", font = font))
            self.gradesTittles[e].place(x = box[e][0], y = box[e][1], anchor = "center")

            e += 1


        self.kanjisButton = []

        font = Font("none", "60", "normal", "roman")
        self.kanjiFocus = tkinter.Label(self.window, text = "", bg = "#f2f2f4", fg = "#2c2c2c", font = font)
        self.kanjiFocus.place_forget()

        self.getKanjisCount += 1

        self.Manager("hide", "menu")
        self.scene = "getKanjis"

    #Draw the kanjis in the window
    def KanjiGrade(self, grade):
        self.grade = grade
        if grade == "1":
            grade = self.ShouGaku1Nen
        elif grade == "2":
            grade = self.ShouGaku2Nen
        elif grade == "3":
            grade = self.ShouGaku3Nen
        elif grade == "4":
            grade = self.ShouGaku4Nen
        elif grade == "5":
            grade = self.ShouGaku5Nen
        elif grade == "6":
            grade = self.ShouGaku6Nen
        elif grade == "Int 1":
            grade = self.ChuuGaku1Nen
        elif grade == "Int 2":
            grade = self.ChuuGaku2Nen
        elif grade == "Int 3":
            grade = self.ChuuGaku3Nen
        elif grade == "Added in 2010":
            grade = self.Added2010

        result = ""
        for i in grade:
            result += i

        #Create main frame
        """
        self.mainFrame = tkinter.Frame(self.window)
        self.mainFrame.pack(fill="both", expand=1)

        #Create Canvas
        self.Canvas = tkinter.Canvas(self.mainFrame)
        self.Canvas.pack(side="left", fill="both", expand=1)

        #Add Scrollbar
        self.Scrollbar = ttk.Scrollbar(self.mainFrame, orient = "vertical", command = self.Canvas.yview)
        self.Scrollbar.pack(side="right", fill="y")

        #Configure Canvas
        self.Canvas.configure(yscrollcommand = self.Scrollbar.set)
        self.Canvas.bind("<Configure>", lambda e: self.Canvas.configure(scrollregion = self.Canvas.bbox("all")))

        #Create ANOTHER frame inside the Canvas
        self.snFrame = tkinter.Frame(self.Canvas)

        #Add frame to canvas window
        self.Canvas.create_window((0, 0), window = self.snFrame, anchor = "nw")"""
        """

        self.scrollbar = tkinter.Scrollbar(self.window)

        self.canvas = tkinter.Canvas(self.window, background = "#ffffff", yscrollcommand = self.scrollbar.set)

        self.scrollbar.config(command = self.canvas.yview)

        self.scrollbar.pack(side = "right", fill = tkinter.Y)

        self.frame = tkinter.Frame(self.canvas)

        self.canvas.pack(side = "left", fill = "both", expand = True)

        self.Canvas.create_window((0, 0), window = self.frame, anchor = "nw")"""


        for i in self.gradesButtons:
            destroy(i)

        for i in self.gradesTittles:
            destroy(i)

        font = Font("none", "12", "normal", "roman")

        e = 0
        a = 0
        y = 10

        yChange = 40 #What value is changed in x
        xChange = 35 #What value is changed in x

        box = []
        for x in range(15, 1000, yChange):
            for i in range(15, self.xSize - xChange, xChange):
                box.append((i, x))

        for i in result:
            self.kanjisButton.append(tkinter.Button(self.window, text = i, bg = "#f2f2f4",  height = 1, underline = -1, fg = "#2c2c2c",bd = "0", relief = "flat", font = font, command = lambda i=i: self.Manager("show", "kanji", i)))
            self.kanjisButton[e].place(x = box[a][0], y = box[a][1])

            #self.kanjisButton[e].bind("<Enter>", self.kanjisButton[e].config(underline = 1))
            #self.kanjisButton[e].bind("<Leave>", self.kanjisButton[e].config(underline = -1))
            e += 1
            a += 1

        self.subScene = "kanjis"

    def Manager(self, hideOrShow, what, kanji = ""):
        print(self.scene)
        if hideOrShow == "show":
            if what == "menu":
                self.scene = "menu"

                #Replace menu
                x = 110
                y = 130
                font = Font("none", "12", "bold", "roman")
                self.GetKanjisButton.place(x = x, y = y, anchor = "nw")
                self.CreateAnkiDeckButton.place(x = 600 - x, y = y, anchor = "ne")
                self.SearchDailyKanjisButton.place(x = 300, y = y + 50, anchor = "n")
                self.tittle.place(x = 300, y = 50, anchor = "center")

                #Hide all other
                self.Manager("hide", "getKanjis")
                self.Manager("hide", "dailyKanjis")
                self.Manager("hide", "anki")

            if what == "kanji":
                self.Manager("hide", "getKanjis")
                self.subScene = "kanjiFocus"
                self.kanjiFocusCount += 1
                self.kanjiFocus.place(x = self.xSize / 2, y = self.ySize / 2, anchor = "center")
                self.kanjiFocus.config(text = kanji)
            if what == "getKanjis":
                destroy(self.kanjiFocus)
                self.KanjiGrade(self.grade)

        elif hideOrShow == "hide":
            if what == "menu":
                destroy(self.GetKanjisButton)
                destroy(self.SearchDailyKanjisButton)
                destroy(self.CreateAnkiDeckButton)
                destroy(self.tittle)

            elif what == "getKanjis":
                if self.getKanjisCount > 0:
                    if self.subScene == "kanjis":
                        #destroy(self.snFrame, "pack")
                        for i in self.kanjisButton:
                            destroy(i)
                    if self.subScene == "kanjiFocus":
                        destroy(self.kanjiFocus)

                    for i in self.gradesTittles:
                        destroy(i)

                    for i in self.gradesButtons:
                        destroy(i)

            elif what == "dailyKanjis":
                if self.dailyKanjisCount > 0:                    
                    for i in self.heisigLabels:
                        destroy(i)

                    destroy(self.kanjisLabel)

                    for i in self.languageButtons:
                        destroy(i)
            elif what == "anki":
                if self.createankiCount > 0:
                    for i in self.kanjisEntry:
                        destroy(i)

                    for i in self.entryTittles:
                        destroy(i)

                    for i in self.languageButtons:
                        destroy(i)

                    destroy(self.languageInstructions)
                    
                    destroy(self.ankiTittle)


    def key_pressed(self, event):
        if event.keycode == 9:
            if self.scene == "menu":
                self.window.destroy()
            elif self.scene != "menu" and self.subScene != "kanjiFocus":
                print("MENU")
                self.Manager("show", "menu")
            elif self.scene == "getKanjis":
                print("GETKANJIS")
                if self.subScene == "kanjiFocus":
                    print("KANJIFOCUS")
                    self.subScene = "kanjis"
                    self.Manager("show", "getKanjis")

    
    def WINDOW(self):
        #Create window
        self.window = tkinter.Tk(className = "-Study Japanese-")
        self.window.geometry(f"{self.xSize}x{self.ySize}")

        self.window.resizable(False, False)
        
        #Set background
        self.window.configure(background = "#f2f2f4")      

        #Create Label
        font = Font("none", "25", "bold", "roman")

        self.tittle = tkinter.Label(self.window, text = "Study Japanese", height = 1, width = 20, bg = "#f2f2f4", fg = "#2c2c2c", font = font)
        self.tittle.place(x = 300, y = 50, anchor = "center")
        #Detect key pressed
        self.window.bind("<Key>", self.key_pressed)

        photo = tkinter.PhotoImage(file = "bitIcon.png")
        self.window.iconphoto(False, photo)
        #self.window.wm_iconbitmap('bitIco.png')


        #Create main buttons
        x = 110
        y = 130
        font = Font("none", "12", "bold", "roman")

        self.GetKanjisButton = tkinter.Button(self.window, text = "Get Jôyô Kanjis", bg = "#ffffff", height = 1, fg = "#2c2c2c",bd = "3", highlightcolor = "#f5f5f5", font = font, command= lambda: self.GetKanjisCommand())
        self.GetKanjisButton.place(x = x, y = y, anchor = "nw")
        
        self.CreateAnkiDeckButton = tkinter.Button(self.window, text = "Create anki deck", bg = "#ffffff", height = 1, fg = "#2c2c2c", bd = "3", highlightcolor = "#f5f5f5", font = font, command= lambda: self.CreateAnkiDeckCommand())
        self.CreateAnkiDeckButton.place(x = 600 - x, y = y, anchor = "ne")
        
        self.SearchDailyKanjisButton = tkinter.Button(self.window, text = "Search the daily kanjis", bg = "#ffffff", height = 1, fg = "#2c2c2c",bd = "3", highlightcolor = "#f5f5f5", font = font, command= lambda: self.DaillyKanjisCommand())
        self.SearchDailyKanjisButton.place(x = 300, y = y + 50, anchor = "n")

        self.window.mainloop()

    def CloseWindow(self):
        window.destroy()
        exit()

#Calculate the days between two dates
def DaysBetween(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y/%m/%d")
    d2 = datetime.datetime.strptime(d2, "%Y/%m/%d")
    return abs((d2 - d1).days)

#Difference between someday and today
def GetDate():
    firstDate = "2021/04/11" #Here you have to enter your begin date
    firstDate = datetime.datetime.strptime(firstDate, "%Y/%m/%d")
    firstDate = firstDate.strftime("%Y/%m/%d")

    today = datetime.date.today()
    today = today.strftime("%Y/%m/%d")

    return DaysBetween(firstDate, today)

#Get daily Kanjis
def DailyKanji(difference):
    result = ""
    beginKanji = 1700 + difference * 5
    endKanji = beginKanji + 5

    result  = ""

    for i in range(beginKanji, endKanji):
        result += AllKanji[i]

    pyperclip.copy(result)
    return result