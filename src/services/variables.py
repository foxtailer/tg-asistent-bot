HELP_MESSAGE_ENG = """
📖 
The bot can store your dictionary and play games with you using the words in this dictionary.\


The dictionary looks like this:\

<code>
1) Cat:Кот (My beautiful cat.)
2) Dog:Собака (Very big dog.)
...
</code>\

(Word, Translation, Example)

You can interact with the bot using the commands menu (≡ Menu) in the bottom-left corner of \
your screen or by typing commands in the chat, like:

<code>/add Help,Помощь,I need help.</code>

In this case, the command will add a new word, "Help," to the dictionary.  
*Note: When adding a word, translation, and example, separate them with a comma. This means \
you cannot use commas in the example sentence.

Each command behaves differently and may require specific arguments. To learn how a command works, \
type 'help' as a parameter for the command.  
*A parameter is a word or letter that comes after a command.

<code>/test help</code>

This will provide a description of the command.

To change bot languege enter <code>/start</code> egein.

I hope this bot helps you enjoy your learning journey! 😊\
"""

HELP_MESSAGE_RUS = """
📖 
Бот может хранить ваш словарь и играть с вами в игры, используя слова из этого словаря.

Словарь выглядит так:

<code>
1) Cat:Кот (My beautiful cat.)
2) Dog:Собака (Very big dog.)
...
</code>

(Слово, Перевод, Пример)

Вы можете взаимодействовать с ботом через меню команд (≡ Menu) в левом нижнем углу экрана\
или вводя команды в чат, например:

<code>/add Help,Помощь,I need help.</code>

В этом случае команда добавит в словарь новое слово "Help".  
*Примечание: При добавлении слова, перевода и примера они разделяются запятой. Это означает,\
что в предложении-примере нельзя использовать запятые.

Каждая команда работает по-разному и может требовать определённых аргументов. Чтобы узнать,\
как работает команда, введите 'help' в качестве параметра к команде.  
*Параметр — это слово или буква, которые идут после команды.

<code>/test help</code>

Это даст вам описание команды.

Надеюсь, этот бот поможет вам наслаждаться вашим путешествием в обучении! 😊
"""

COMANDS = (
    'help',
    'test',
    'shuffle',
    'show',
    #'verbs',
    'add',
    'del',
    'start',
    #'sentense',
    #'get_example',
)

COMAND_TITLES_EN = (
    'Help/Info',
    'Test throw selected day',
    'Try to guess shuffled word',
    'Show dictionary',
    #'Learn irregular verbs',
    'Add new words in dict',
    'Delete word/words',
    'Start bot',
)

COMAND_TITLES_RU = (
    'Помощь/Информация',
    'Тест по выбранному дню',
    'Попробуйте угадать перемешанное слово',
    'Показать словарь',
    'Учить неправильные глаголы',
    'Добавить новые слова в словарь',
    'Удалить слово/слова',
    'Запустить бота',
)

# Base forms
V1 = (
    "abide","be","bear","beat","become","begin","bend","bet","bid","bind","bite","bleed","blow","break",
    "breed","bring","broadcast","build","burn","burst","buy","catch","choose","cleave","cling","come",
    "cost","creep","cut","deal","dig","do","draw","dream","drink","drive","dwell","eat","fall","feed",
    "feel","fight","find","flee","fling","fly","forbid","forget","forgive","forsake","freeze","get",
    "give","go","grind","grow","hang","have","hear","hide","hit","hold","hurt","keep","kneel","know",
    "knit","lay","lead","lean","leap","learn","leave","lend","let","lie","light","lose","make","mean",
    "meet","mistake","pay","put","read","rid","quit","ride","ring","rise","run","saw","say","see","seek",
    "sell","send","set","sew","shake","shed","shine","shoot","show","shrink","shut","sing","sink","sit",
    "slay","sleep","slide","sling","smell","smite","sow","speak","speed","spend","spell","spill","spin",
    "spit","split","spoil","spread","spring","stand","steal","stick","sting","stink","strike","swear",
    "sweep","swell","swim","swing","take","teach","tear","tell","think","throw","thRUSt","tread",
    "understand","wake","wear","weave","wed","weep","win","wind","wring","write")

# Past simple forms
V2 = (
    "abode/abided","was/were","bore","beat","became","began","bent","bet","bid/bade","bound","bit","bled",
    "blew","broke","bred","brought","broadcast","built","burnt","burst","bought","caught","chose",
    "cleaved/clove","clung","came","cost","crept","cut","dealt","dug","did","drew",
    "dreamt/dreamed","drank","drove","dwelt/dwelled","ate","fell","fed","felt","fought","found","fled",
    "flung","flew","forbade","forgot","forgave","forsook","froze","got","gave","went","ground","grew",
    "hung","had","heard","hid","hit","held","hurt","kept","knelt","knew","knitted/knit","laid","led",
    "leaned/leant","leapt/leaped","learnt/learned","left","lent","let","lay","lit","lost","made","meant",
    "met","mistook","paid","put","read","rid","quit","rode","rang","rose","ran","sawed","said","saw",
    "sought","sold","sent","set","sewed","shook","shed","shone","shot","showed","shrank/shrunk","shut",
    "sang","sank","sat","slew","slept","slid","slung","smelt","smote","sowed","spoke","sped","spent",
    "spelt/spelled","spilt/spilled","spun","spat","split","spoilt/spoiled","spread","sprang","stood",
    "stole","stuck","stung","stank","struck","swore","swept","swelled","swam","swung","took","taught",
    "tore","told","thought","threw","thRUSt","trod","understood","woke","wore","wove","wed/wedded","wept","won","wound","wrung","wrote")

# Past participle forms
V3 = (
    "abidden/abided","been","born","beaten","become","begun","bent","bet","bid/bidden","bound","bitten",
    "bled","blown","broken","bred","brought","broadcast","built","burnt","burst","bought","caught",
    "chosen","cleaved/cloven","clung","come","cost","crept","cut","dealt","dug","done","drawn",
    "dreamt/dreamed","drunk","driven","dwelt/dwelled","eaten","fallen","fed","felt","fought","found",
    "fled","flung","flown","forbidden","forgotten","forgiven","forsaken","frozen","got","given","gone",
    "ground","grown","hung","had","heard","hidden","hit","held","hurt","kept","knelt","known",
    "knitted/knit","laid","led","leaned/leant","leapt/leaped","learnt/learned","left","lent","let","lain",
    "lit","lost","made","meant","met","mistaken","paid","put","read","rid","quit","ridden","rung",
    "risen","run","sawn/sawed","said","seen","sought","sold","sent","set","sewed/sewn","shaken","shed",
    "shone","shot","shown","shrunk/shrunken","shut","sung","sunk","sat","slain","slept","slid","slung",
    "smelt","smitten","sown/sowed","spoken","sped","spent","spelt/spelled","spilt/spilled","spun",
    "spat","split","spoilt/spoiled","spread","sprung","stood","stolen","stuck","stung","stunk",
    "struck/stricken","sworn","swept","swollen","swum","swung","taken","taught","torn","told","thought",
    "thrown","thRUSt","trodden","understood","woken","worn","woven","wed/wedded","wept","won","wound","wrung","written")

V2_sentences = (
    "He abode by the rules.","They were very tired.","She bore the pain bravely.","He beat the drum loudly.",
    "She became a teacher.","They began the work early.","He bent the wire.","I bet on the wrong team.",
    "He bade us goodbye.","She bound the package.","The dog bit him.","His finger bled.",
    "The wind blew hard.","She broke the glass.","They bred horses.","She brought a gift.",
    "The news broadcast live.","They built a house.","The fire burnt out.","The balloon burst.",
    "I bought food.","She caught the ball.","He chose wisely.","The knight clove the log.",
    "The child clung to her.","He came late.","The trip cost a lot.","The cat crept quietly.",
    "She cut the paper.","He dealt the cards.","They dug a hole.","She did her homework.",
    "He drew a picture.","I dreamt about home.","He drank water.","She drove fast.",
    "They dwelt there.","He ate dinner.","She fell down.","He fed the dog.",
    "She felt cold.","They fought bravely.","He found the keys.","She fled the city.",
    "He flung the rope.","Birds flew south.","He forbade smoking.","She forgot the date.",
    "He forgave her.","They forsook the village.","Water froze.","He got angry.",
    "She gave help.","They went home.","He ground the coffee.","The plant grew fast.",
    "He hung the picture.","She had time.","He heard a noise.","She hid the money.",
    "He hit the ball.","She held the baby.","He hurt his arm.","She kept the secret.",
    "He knelt down.","She knew the answer.","She knit a scarf.","She laid the book down.",
    "He led the group.","He leant on the wall.","He leapt over it.","She learnt English.",
    "He left early.","She lent money.","She let him go.","The dog lay down.",
    "She lit the candle.","He lost hope.","She made a cake.","He meant well.",
    "They met yesterday.","He mistook me.","She paid cash.","She put it there.",
    "I read the note.","He rid the room of dust.","He quit his job.","She rode a horse.",
    "The bell rang.","The sun rose.","He ran fast.","He sawed wood.",
    "She said nothing.","He saw a bird.","He sought help.","She sold fruit.",
    "He sent a letter.","She set the table.","She sewed the dress.","He shook my hand.",
    "The snake shed skin.","The sun shone.","He shot once.","She showed me.",
    "The market shrank.","The door shut.","They sang loudly.","The ship sank.",
    "He sat down.","He slew the dragon.","She slept well.","He slid on ice.",
    "He slung the bag.","It smelt bad.","He smote the bell.","He sowed seeds.",
    "She spoke clearly.","He sped away.","She spent money.","He spelt the word.",
    "She spilt milk.","She spun around.","He spat angrily.","The glass split.",
    "The milk spoilt.","The fire spread.","He sprang up.","He stood firm.",
    "He stole bread.","She stuck the note.","The bee stung him.","The trash stank.",
    "He struck the wall.","He swore loudly.","She swept the floor.","The river swelled.",
    "He swam far.","The door swung.","He took notes.","She taught math.",
    "He tore paper.","She told the truth.","He thought deeply.",
    "She threw the ball.","He thrust the knife.","He trod carefully.",
    "She understood me.","He woke early.","He wore a coat.",
    "She wove fabric.","They wed quietly.","She wept softly.",
    "He won easily.","He wound the clock.","He wrung the cloth.",
    "She wrote a letter.")

V3_sentences = (
    "He has abidden the law.","She has been here.","He was born here.","The drum was beaten.",
    "She has become famous.","They have begun work.","The metal is bent.","The price was bet.",
    "He was bidden to come.","The rope is bound.","He was bitten.","She has bled.",
    "The balloon has blown up.","The glass is broken.","Dogs are bred here.",
    "The gift was brought.","The match was broadcast.","The bridge is built.",
    "The toast is burnt.","The pipe has burst.","The food was bought.",
    "He was caught.","She was chosen.","The tree was cloven.",
    "The child has clung.","He has come back.","It has cost much.",
    "The cat has crept.","The cake is cut.","Cards were dealt.",
    "The hole is dug.","The work is done.","The picture is drawn.",
    "I have dreamt of home.","He has drunk tea.","The car was driven.",
    "They have dwelt there.","The food is eaten.",
    "She has fallen.","The dog is fed.","I have felt better.",
    "The battle was fought.","The keys are found.",
    "He has fled.","The stone was flung.",
    "The birds have flown.","Smoking is forbidden.",
    "The date is forgotten.","She is forgiven.",
    "The town was forsaken.","The lake is frozen.",
    "He has got help.","The gift is given.",
    "They have gone.","The wheat is ground.",
    "The plant has grown.","The coat is hung.",
    "She has had lunch.","The sound was heard.",
    "The money is hidden.","The ball was hit.",
    "The baby is held.","He was hurt.","The secret is kept.",
    "He has knelt.","The answer is known.",
    "The scarf is knit.","The book is laid down.",
    "The team is led.","He has leant forward.",
    "The fence was leaped.","English is learnt.",
    "He has left.","The money is lent.",
    "He is let go.","The dog has lain down.",
    "The candle is lit.","Hope is lost.",
    "The cake is made.","It was meant well.",
    "They have met.","The error was mistaken.",
    "The bill is paid.","The box is put here.",
    "The sign was read.","The room is rid of dust.",
    "He has quit.","The horse is ridden.",
    "The bell has rung.","The sun has risen.",
    "He has run.","The board was sawn.",
    "The word was said.","The bird was seen.",
    "Help was sought.","The house is sold.",
    "The letter is sent.","The table is set.",
    "The dress is sewn.","The bottle was shaken.",
    "The skin was shed.","The light has shone.",
    "He was shot.","The way was shown.",
    "The size has shrunk.",
    "The door is shut.","The song was sung.",
    "The ship has sunk.","He has sat down.",
    "The dragon was slain.",
    "She has slept.","The ice was slid on.",
    "The bag was slung.","It has smelt bad.",
    "He was smitten.","The field is sown.",
    "The truth was spoken.",
    "He has sped away.","The money is spent.",
    "The word is spelt.",
    "Milk was spilt.","The thread is spun.",
    "He has spat.","The wood is split.",
    "The food is spoilt.","The fire has spread.","He has sprung up.",
    "He has stood firm.","The jewels were stolen.","The note is stuck.",
    "He was stung.","The place has stunk.","The bell was struck.",
    "He has sworn.","The floor is swept.","The river has swollen.",
    "He has swum.","The door has swung.","The prize is taken.",
    "She has taught well.","The paper is torn.","The truth is told.",
    "It was thought over.","The ball was thrown.","The knife is thrust.",
    "The path is trodden.","She is understood.","He has woken up.",
    "The coat is worn.","The cloth is woven.",
    "They are wed.","She has wept.","He has won.",
    "The toy is wound.","The towel is wrung.","The book is written."
)

