---
title: Twitter community notes
---

Proposed [Twitter community notes](https://twitter.com/i/communitynotes/download-data) from the last week, updated regularly. _[More…]({{ '/about/' | relative_url }})_

<div class="table-responsive">
  <table id="notes-table" class="table table-striped" data-order='[[ 0, "desc" ]]'>
    <thead>
      <tr>
        <th>Note created</th>
        <th>Note shown</th>
        <th>Tweet</th>
        <th>Note</th>
        <th>Reason for note</th>
        <th>Tweet language</th>
        <th>Tweet status</th>
        <th>Username</th>
        <th>Tweet content</th>
        <th>Total ratings</th>
        <th>Tweet author</th>
      </tr>
    </thead>
    <tbody>
    </tbody>
  </table>
</div>

<script>
  const candidates = ['SKinnock', 'AbigailMainon', 'VoteCharlieAbel', 'KirstySNP', 'DesBouse', 'Lucas_S_Grant', 'Esme_Houston_', 'gilltebberen4NE', 'LTLabour', 'david_duguid', 'shaylogan', 'StephenFlynnSNP', 'guy_ingerson', 'councillormalik', 'WheelerJohn_', 'AnumSNP', 'shottsman7', 'LeoDochertyUK', 'tlloydjones', '_joebelcher', 'LJDLabour', 'Grahameardley', 'ablibdems', 'morton_wendy', 'VoteEvaForAandG', 'CllrBLeishman', 'KennyMacAskill', 'MrJohnNicolson', 'JaneBrophyLD', 'CogginsGeraldin', 'cdrand', 'PSwansborough', 'CllrKarl', 'richardmarbrow', 'JackMorrisCymru', 'marktamimp', 'LFarnz', 'McGuinnessGreen', 'nigelmills', 'KateSmithLibDem', 'labourlizzie', 'DaveDooganSNP', 'RealStephenKerr', 'kenneth_morton', 'danspena', 'RickyJBrooks', 'C4Cruickshank', 'StephenGethins', 'GhaziAlba', 'amandahampsey', 'hamish4ABSL', 'BrendanOHaraMP', 'AlanReidAandB', 'griffitha', 'Christophherr', 'LeeAndersonMP_', 'RheaKeehn', 'DamianGreen', 'tristram4reform', 'sojanuk', 'voteconsensus', 'GreenMandyRossi', 'DominicHardwick', 'LeeAlanHuntbach', 'angelarayner', 'RobBAylesbury', 'laurakyrkesmith', 'elainestewart2', 'Corri_Wilson', 'lfbadams', 'AJBWestOxGreens', 'North_Oxon', 'VictoriaPrentis', 'SEANLWOODCOCK', 'TJohnClark', 'NWWGreenParty', 'clairehughesBA', 'mostyn11', 'RobinMillarMP', 'RachAnneRoberts', 'catwager', 'CharleyHasted', 'CllrDRodwell', 'nomeantom', 'DanJarvisMP', 'steph_peacock', 'simonfell', 'BarryMorga46644', 'MichelleScrog1', 'BarrowGreens', 'StewGBillericay', 'AlexHarrisonLCN', 'EKSainsbury', 'MariaMillerUK', 'LukeMLabour', 'RichardMWhelan1', 'Bren4Bassetlaw', 'BassetlawGreen', 'helen4bassetlaw', 'CllrJoWhite', 'dan_bewley', 'Wera_Hobhouse', 'DominicTristram', 'JPBWFarm', 'MartynDaySNP', 'thejohnhannah', 'SimonJay4BGL', 'LibDemSally', 'kittysull1', 'FrancisChubb', 'Marshadecordova', 'tom_pridham', 'AVCrabtree', 'johnashalsall', 'joymorrissey', 'EdwardReformuk', 'RuthFabricant', 'jhannahgray', 'ChloeJane_Ross', 'pinder_chauhan', 'BedfordVann', 'YasinForBedford', 'SeamasBelfast', 'naomi_long', 'GRobinsonDUP', 'Briansmyth99', 'PhillipBrett21', 'johnfinucane', 'NualaMcAllister', 'oharamal', 'DansBoucher', 'AineGroogan', 'ClaireHanna', 'tracybelfast1', 'KateNicholl', 'GerryCarrollPBP', 'PaulDoherty___', 'PaulMaskeyMP', 'FMcCoubrey1', 'EoinM04', 'RachelBentleyNB', 'coyleneil', 'DrJonathanIliff', 'BordersRayLD', 'John2Win', 'EM4BRS', 'caitlinstottBRS', 'DavidWilsonSNP', 'mohammedakunjee', 'rushanaraali', 'RabinaKhan', 'jonmabbutt', 'ElizabethWaight', 'ChrisCollin82', 'denishealy', 'roger_hoe', 'MargaretPinder', 'grahamstuart', 'LabourBayliss', 'TheGoodStatsMan', 'BeckyJ1567060', 'Jolph', 'tomebright', 'danfrancis02', 'davidmcbride1', 'jamesmutimerWPB', 'rbrharrison', 'IanMiddletonX', 'CalumMillerLD', 'visioncampaigns', 'JoBirdJoBird', 'ideallythissss', 'S_E_Kelly', 'Alison_McGovern', 'ReformUKBhead01', 'PreetKGillMP', 'ColinGreenLD', 'JoeKirbyReform', 'ashvir_sangha', 'VoteDrAmmar', 'Jack4Erdington', 'PauletteHamilto', 'srknee', 'TahirAliMP', 'gardensinboots', 'HenryMorris', 'liambyrnemp', 'JamesGilesRBK', 'leedargue', 'BirminghamLadyW', 'shabanamahmood', 'Akhmedyakoob1', 'RobGrant_Green', 'GarySambrook89', 'KefentseDennis', 'khalid4PB', 'kamelhawwash', 'simonphippss', 'yvonne_clements', 'rogerbhx', 'jodymcintyremp', 'jessphillips', 'SamJRushworth', 'kate_hollernmp', 'adamjtslack', 'iaincdonaldson', 'CreserDylanGrn', 'BeaversLorraine', 'PaulMaynardUK', 'tinalouiseUK', 'Andrew_Cregan', 'ChrisWebbMP', 'CllrjackieC', 'hannahhjjarvis', 'blaenaugwentmp', 'liztwistmp', 'IanLaveryMP', 'SLeylandGreen', 'PeartBlyth', 'GreenCarolBirch', 'davidkurten', 'clarewalshlab', 'Nataliefleet', 'DavidKesteven', 'Reaneyandson', 'BneIndependent', 'kirith_ae', 'BeckyForrestLD', 'manchester453', 'YasminQureshiMP', 'vickiattenborou', 'Phil_Brickell', 'DylEvans_', 'CGreenUK', 'NeilDoolin1', 'peter_dowd', 'AlexFawbert', 'richlloyd', 'TiceRichard', 'mattwarman', 'Tobias_Ellwood', 'cllrtomhayes', 'martinhoulden', 'pe_nng', 'CllrKWilson', 'ConorBurnsUK', 'JessicaToale', 'KatieBracknell', 'SamuelMunyeza', 'JamesSunderl', 'PDJSwallow', 'bradfordgreens', 'Imran_HussainMP', 'Harry_Boota', 'judithcummins', 'greenmattbfd', 'ImadAhmed', 'nazshahbfd', 'JamesCleverly', 'k_afranks', 'MatthewKWright', 'LibDemDavid', 'MatthewDorrance', 'emilyvdurrant', 'JonesyFay', 'BRgreenparty', 'BrentGreens', 'DawnButlerBrent', 'LauraBlumenthal', 'RuthCadbury', 'kuldev_sehra', 'FreyaSummersgil', 'barrygardiner', 'KlokNadia', 'GarethPBarrett', 'alexburghart', 'paulngodfrey', 'LibDemsBwd', 'RobinTilbrook', 'CPJElmore', 'CarolineJonesMS', 'CllrSamTrask', 'pelepjb', 'Ashley7Fox', 'Bridgwater_Lab', 'ClairedeSully', 'mariabowtell', 'charliedewhirst', 'Cllr_Tim_Norman', 'DoreJayne', 'Carlo_Verda1', 'MartinVickers', 'SaltdeanLibDems', 'Khobi_Vallis', 'wardchr82', 'sianberry', 'CBuck_SDP', 'mrtomgray', 'ashleyridley5', 'ThangamDebb', 'carla_denyer', 'DanConaghan', 'KerryMP', 'damienegan', 'LouiseLibDem', 'TommyTrueman90', 'carogucc', 'darrenpjones', 'Mary4BristolNW', 'LRSaunders23', 'breitideas', 'LizBrennan28897', 'andrewbrownld', 'NEILSDPBRIS84', 'KarinSmythMP', 'JeromeMayhew', 'iainsimpson', 'ReformBromley', 'PeterTFortune', 'JulieIreland', 'OanaOlaru92', 'caroline_sandes', 'TaliaEllisGreen', 'NeenaGmep', 'djnicholl', 'BradleyThomasUK', 'AheeshaZ67256', 'NBelfitt', 'OwenBrett1', '_LewisCocking', 'catdeakin', 'julietocampbell', 'DarrenG_Henry', '_CallumAnderson', 'domdyer70', 'Amanda_Spoke', 'iainastewart', 'GBirtwistle', 'antony_hig', 'OliverRyanUK', 'jacob_collier_', 'mintmurray4', 'HealeyMark4', 'JamesDalyMP', 'JamesFrith', 'Owain4Hale', 'SteMorris', 'andrew4bury', 'Dan_Ross_CPB', 'ArnoldSaunders5', 'Christian4BuryS', 'mikeymagnetic', 'ReformBury_Stow', 'bizmcd', 'peterprinsley', 'Simonhartmp', 'MarthaAngharad', 'steve_aich', 'chrisevansmp', 'Lindsay_Whittle', 'liusaidhbeattie', '929Eva', 'ReformHighlands', 'Jamie4North', 'AnneTho39135248', 'JoshFG', 'vanessalee4mp', 'CalderGreens', 'cdonnithorne1', 'thaliasimone1', 'Perran4CRH', 'shanemanning', 'CllrPayne', 'danielzeichner', 'ReformUKCannock', 'amandamilling', 'CllrJoshNewbury', 'RosieDuffield1', 'LouHarvey_Q', 'HenryStantonGP', 'rodneyberman', 'samcoatescymru', 'CadewynElS', 'jostevenslabour', 'annamcmorrin', 'MegSFoster36', 'JoelTory', 'SDoughtyMP', 'as_penarth', 'atw888', 'jamesrobhamblin', '_peterhopkins', 'KataAkil', 'julie4Carlisle', 'John4Carlisle', 'BrianUkulele', 'im_sfk', 'ElliotColburn', 'Bobby_Dean', 'suttongreens', 'stevekSDP', 'HershThaker', 'RebeccaHarrisMP', 'alangemmell', 'Annie4Ayrshire', 'olliepearson', 'MelJStride', 'GillMWestcott', 'Mark4Devon', 'KevinCraigUK', 'TaghridAlMawed', 'JackieJonesWal1', 'BenMLake', 'CllrAledT', 'mark4ceredigion', 'NathanGamester', 'ReformChatham', 'cllrtrisosborne', 'SteveTanner_SDP', 'kelly4labour', 'ThomasMorrison', 'MaryRobinson01', 'vickyford', 'mariecgoldman', 'DarrenReform', 'blaisebaquiche', 'ChelFulhamBen', 'GregHands', 'AlexChalkChelt', 'larachaplin', 'mpmwilko', 'chillychrisy', 'SarahGreenLD', 'GarethWatBucks', 'IanBarfield', 'Ben_Flook', 'tobyperkinsmp', 'maximusdogface2', 'cwacgreen', 'SamanthaDixonMP', 'simonjveardley', 'sgribbonlibdems', 'AphraBrandreth', 'robherdch3', 'JessBrownFuller', 'ThomasCollinge', 'GillianKeegan', 'WSussexBrexit', 'cbrody', 'MPIainDS', 'ShamaTatler', 'DeclanBaseley', 'NicPuntis', 'way2ravi', 'mrkdurrant', 'dfarb', 'RUKChipBarnet', 'RichardHewison', 'Dan4Barnet', 'blrhc', 'LindsayHoyle_MP', 'mwt2008', 'mikefcox', 'JoHoward2016', 'VoteTimBarnes', 'RNBlake', 'edwardlucas', 'bepipezzulli', 'ReformCTDurham', 'Jonathan_Elmer', 'marykfoy', 'LukeHolmes', 'AMack30294', 'NatashaOsben', 'ClactonLabour', 'GilesWatling', 'ben_curtis_1', 'BellRibeiroAddy', 'flntshrelibdems', 'JamesDavies', 'becky_gittins', 'ClwydEast', 'gillgerman_', 'NWWGreenParty', 'DarrenMillarMS', 'JOrangeReformUK', 'paul_rowlinson', 'CllrDaveWilkins', 'StevenBonnarSNP', 'LeoLanahan', 'FJMcNally', 'jamescracknell', 'MartinGossCol', 'RUK_Colchester', 'StuartHaleYCM', 'JasonMcCartney', 'richgmccarthy1', 'S_A_Russell', 'MartinReform', 'LeeBarronLabour', 'VotePursglove', 'MaryCreagh_', 'GreenXian', 'Isufyan1', 'tomholder', 'TaiwoOwatemi', 'MattieHeaven', 'MellonSdp6741', 'SJRichmond89', 'zarahsultana', 'BackhouseSNP', 'MagsSGP', 'JNHanvey', 'melanie_ward', 'ThomForCastle', 'efoody', 'ZackAliUK', 'LindaBamieh', 'CllrPetesTweets', 'arrowmaker76', 'dogsdinnercrewe', 'connor_naismith', 'Matthew_LibDem', 'MatthewPeterWoo', 'JasonCroydonCon', 'scottholman90', 'NDIrons', 'AndrewJPelling', 'GreenPeterU', 'denisegarrod', 'r1ckh0ward', 'CPhilpOfficial', 'BenJLTaylor', 'SimonJTFox', 'LabourSJ', 'magicmarz', 'Stuart_McDonald', 'katrinamurray71', 'samhollanduk', 'Margaret4dr', 'lola__mcevoy', 'benramanauskas', 'MatthewSnedker', 'ReformDarlo', 'Jim4Dartford', 'Laura_Edie8', 'GarethJohnsonMP', 'jharrislibdem', 'marianne_kimani', 'catkinson80', 'DerbyGreens', 'ASollowayUK', 'KeldaE', 'rjcourt52', 'Dines4Dales', 'rachelelnaugh', 'EdwardOakenful1', 'HWetherallTFP', 'WhitbyJmwhitby', 'CllrAlanG', 'Jmullers93', 'joenaitta', 'BaggyShanker', 'DerbyChrisW', 'cllrammar', 'simonjcope', 'heather4db', 'JRThackray', 'samculham', 'OllyGloverLD', 'david4wantage', 'MockyKhan', 'NickAllen1987', 'SallyJameson', 'gregruback', 'NickFletcherMP', 'LeePitcher9', 'NicolaJTurner', 'BluffGlenn', 'Ed_Miliband', 'nadiaburrell', '_chris_coghlan', 'marisaheath06', 'cllrLisaScott', 'pjameslibdem', 'GreensDoverDist', 'MikeTappTweets', 'NeilGreenMidWor', 'HuddlestonNigel', 'Aaaftabhussain', '_SoniaKumar', 'marcolonghi4dn', 'ReformUKDudley', 'pete556', 'LibDemDonna', 'helenhayes_', 'TraceyLittleSNP', 'DGlibdems', 'Laura_Moodie', 'dashmolean', 'DrummondBegg', 'dan4dct', 'dakppc', 'VoteKim4DCT', 'DavidMundellDCT', 'ChrisLawSNP', 'rbmccready', 'jim_mcfarlane99', 'locheeagr', 'RyanBlackadder', 'cllrdownie', 'THeald90', 'EmmaMidBeds', 'alexlmayer', 'reformukDandLB', 'AndrewSelous', 'lucymur76791660', 'LSRPlaid', 'rupahuq', 'NadaJarche', 'LibDemAlastair', 'jwindsorclive', 'HelmiAlharahshe', 'Samehahabeeb', '___MariaKhan__', 'jamesmurray_ldn', 'CraigODonnell88', 'GeorgieCalle', 'OfSouthall', 'pedrodc2024', 'deirdrecostigan', 'DrTariq_Mahmood', 'Neil4W7andW13', 'CllrPauline', 'Tahirmaher2', 'YuanfenYang', 'JoanneHowey', 'grahamemorris', 'RUKEasington', 'DannyDonnelly1', 'a_margaretanne', 'johnstewartuup', 'eastantrimmp', 'Caroline_Ansell', 'JoshBabarinde', 'EastbourneGreen', 'bscox', 'mimsdavies', 'BenedictDempsey', 'TahirMirza01', 'DanielOxleyTBP', 'SotonGreenParty', 'stephenctimms', 'DamianHinds', 'RichardKnightGP', 'LucySimsEHants', 'GrantDCostello', 'LizJarvisUK', 'ShearerDan7', 'CaraHunterSDLP', 'KathleenMcGurk', 'alliancerichard', 'Sandeshgulhane', 'blairmcdougall', 'kirstenoswald', 'allanrmsteele1', 'coletteisp', 'thomasbowell', 'ClaireCoutinho', 'GreenKnight2010', 'clairemalcomson', 'pollyblab', 'PeteForceJones', 'davidkinnairdLD', 'danny__kruger', 'RobNewmanLab', 'tomrutland', 'amandafgrimm', 'chrismurray2010', 'TommySheppard', 'derekwinton', 'mikealibdem', 'DeidreBrock', 'nieldeepnarain', 'tracygilbert72', 'AlanGMelville', 'KayleighFONeill', 'CouncillorCowdy', 'phil_m_holden', 'SimitaSKumar', 'IanMurrayMP', 'JoPhillipsSG', 'CllrScottArthur', 'joannaccherry', 'CllrDanHeap', 'RichardCLucas', 'suejwebber', 'BruceRoyWilson', 'Michael4EdWest', 'euanhyslop', 'cajardineMP', 'ScoLibertarian', 'kvisleis', 'lukebaln', 'KateOsamor', 'cllrccarubia', 'HarryRossGorman', 'NickGoulding4', 'justinmadders', 'AbbateUlysse', 'CharlieJSDavis', 'CliveEfford', 'RealMGSimpson', 'lucyfrazermp', 'ElizabethMcWill', 'ReformUKEnfield', 'feryalclark', 'ChrisDey4Grange', 'GRussoLD', 'DoreRosalind', 'EdPond4EF', 'jon_whitehouse', 'mhairijoanna', 'helenemaguire', 'helenemaguire', 'thatginamiller', 'MarkTodd_pol', 'JamesArcherLD', 'BrentPoland1', 'adamthompson111', 'maggie_erewash', 'richardjmark', 'abenaopp', 'john_cope', 'elthornepr', 'monicabeharding', 'NSGreenParty1', 'WillAczel', 'steve_race', 'TessaDTucker', 'paularnottLD', 'dallimorehelen1', 'eastdevongreens', 'David__Reed', 'Reforminator', 'CllrDanWilson', 'jamesbundy', 'ToniGiugliano', 'Euan4FKSouth', 'SuellaBraverman', 'alexdjust', 'GregoryStafford', 'KhalilYousuf', 'MDawkinsLabour', 'HannahPerkin', 'iamhannahtemple', 'Helen_Whately', 'Reva_Gudi', 'Seemamalhotra1', 'cockneyactivist', 'dhruv4mp', 'PrabhdeepReform', 'EddieRoofe', 'CHazelgrove', 'JackLopresti', 'sarahcreates', 'sarahsackman', 'DamianCollins', 'LarryNgan1', 'anthonymv1', 'Mark_J_Harper', 'ChrisAMcFarling', 'SandraDuffySF', 'columeastwood', 'raichfer87', 'shaunharkin17', 'jannymonty', 'MartinDimery', 'Robin34t', 'tomcalver', 'mgjewellLD', 'EdwardLeighMP', 'jessmcguire01', 'Markfergusonuk', 'MichaelPayneUK', 'Tom_Randall', 'medwaygreens', 'Rehman_Chishti', 'naushabah_khan', 'Peter88902568', 'johnadgrady', 'CllrTKerr', 'askettyles', 'DavidLinden', 'MOwenWPB', 'iris_frs', 'MartinRhodes21', 'alisonthewliss', 'MBGlasgowNE', 'AnneMcLaughlin', 'NiallChristie1', 'Dhruva4alba', 'StewartMcDonald', 'GordonMcKee_', 'VoteSocialist', 'zubirahmed', 'john_hamelink', 'MamunRashidMBE', 'ChrisStephens', 'PJFerguson18', 'FatenHameed3', 'CMonaghanSNP', 'jonfcousins', 'SarahDykeLD', 'halhooberman', 'fayepurbrick', 'Baker4Lab', 'johnbearesnp', 'steve040167', 'RichardGrahamUK', 'alexmclabour', 'Reb_Trimnell', 'ReformGodalming', 'PaulDFollows', 'Jeremy_Hunt', 'JamesLWalsh', 'DavidDavisMP', 'liam_draycott', 'NurulHoqueAli1', 'Harriet4Gor_Buc', 'RThomsonMP', 'GwynneMP', 'cj_dinenage', 'toniaantoniazzi', 'banzaf1', 'GarethDavies_MP', 'graveshamtories', 'drake_rebe66784', 'ReformGravesham', 'ukonu_obasi', 'drlsullivan', 'lia_nici', 'Melanie_Onn', '_JamesTClark', 'keircozens', 'RupertLowe10', 'chris_annous', 'mtpennycook', 'zoefranklinld', 'SHGillinson', 'HackneyAbbott', 'a4antoinette', 'RebeccaJones_03', 'meg_hilliermp', 'Peter_Smorthit', 'AlexBallinger_', 'GreenEmmaB', 'JamesMorris', 'Ryaphor', 'Kate_Dearden', 'martinhey1966', 'hazel__sharp', 'pauljholmes', 'kateneeeedham', 'dgalvanise', 'rossclarksnp', 'imogenwalker', 'ElleAitch8', 'AWNDinsmore', 'AnthonyMGoodwin', 'Naranee2018', 'HammersmithAndy', 'ScottEmery92', 'tulipsiddiq', 'donSwissCottage', 'PhilKnowlesLD', 'RedbreastRobin', 'NeilDotObrien', 'hajirapiranie', 'darrenwoodiwiss', 'ReformHarlowUK', 'yazzyg', 'RiadMannan', 'chrisjvince', 'TweetingCollins', 'NigelforHB', 'pdehoest', 'tomgordonLD', 'AJonesMP', 'shanoakes', 'reetenbanerji', 'BobBlackman', 'PrimeshPatel', 'pamelafitz4HW', 'GarethThomasMP', 'jonathanbrash', 'medwaygreens', 'alexdiner1987', 'bernardjenkin', 'helenadollimore', 'Lucian_Fern', 'SallyAnn1066', 'StefHarv4Havant', 'AlanMakMP', 'john_perry_uk', 'Gayathri4Havant', 'LonLibDemAgent', 'Rizwanakarim1', 'johnmcdonnellmp', 'dizzymum56', 'paulathans', 'Lisa_Smart', 'ClaireVibert', 'hemellibdems', 'SheriefHassan', 'McivorJaymey', 'davidtaylor85', 'noel_willcox', 'GreenGabBail', 'EnderbyClareine', 'Ameet_Jogia', 'ShayaPearl', 'davidpintod', 'ManleyNanda', 'fivanmierlo', 'HerefordLabour', 'Jesse_Norman', 'CllrDanPowell', 'diana4hereford', 'AngieCurwen1', 'SirRogerGale', 'BetterWayOf', 'helenforthanet', 'NicholasCox1961', 'joshdeanuk', 'JulieMarsonMP', 'OliverDowden', 'EmmaMatanle', 'darrenselkus', 'JoshDTapper', 'WilliamClouston', 'cott_nick', 'joe_morris91', 'GuyOpperman', 'elsieblundell', 'CF4HMN', 'StevePotter_RUK', 'laurabeth_t', 'robertlargan', 'jon4highpeak', 'drlukeevans', 'miketmullaney', 'rebecca_pawley', 'BimAfolami', 'CharlesBunker', 'Lucas4HertStort', 'alistrathern', 'charlieclinton', 'AF4HSP', 'Daves1412', 'Keir_Starmer', 'JakeBonetta', 'RichardFoordLD', 'henrygentgreen', 'simonjamesjupp', 'SunnyBrarUK', 'JuliaLopezMP', 'ReformUpminster', 'Dawn_Barnes', 'CatherineWest1', 'jamesfield83', 'QcattQ', 'ricardobradley', 'bphillipsonMP', 'ReformUKSun', 'peterkyle', 'tanushkamarah', 'clrandrewcooper', 'harpreetkuppal', 'markargentLibDe', 'LabourAlexB', 'BenObeseJecty', 'ReformUK_Hunts', 'SarBritcliffeMP', 'Hyndburnrefrm', 'WallerBeth', 'rachel_shares', 'frasercoppin', 'wesstreeting', 'Alex4CandA', 'jas_athwal', 'RichBJC', 'rajmasudforhad', 'SayeedZaman8', 'SiddiqiSyed', 'ronniecowan', 'martinmccluskey', 'ChrisMcEleny', 'ross_stalker', 'drewhendrySNP', 'angusmacdlibdem', 'pajnewman', 'Ruraidh_Stewart', 'jackabbott90', 'tomhunt1988', 'ipsneedsreform', 'james4suffolk', 'EBrothersLabour', 'VixL', 'SarahMorrisIOW', 'JoePJRobertson', 'CameronPalin', 'RichardQuigle18', 'IoWBobSeely', 'Wightactivist', 'VikasAggarwalLD', 'jeremycorbyn', 'prafulnargund', '_martynnelson', 'carneross', 'TerryStacyLD', 'EmilyThornberry', 'Conway_NE', '_niccook', 'KateOsborneMP', '_RobbieMoore', 'CatParrott', 'JennyWLibDem', 'monaadam68', 'FelicityBuchan', 'emmadentcoad', 'WilliamHoungbo', 'josephpowell', 'EmForMP', 'merf_sdp', 'rosie_wrighting', 'AlanBrownSNP', 'JordanDCowie', 'ljonesy70', 'EdwardJDavey', 'helenedwardcwo', 'EuniceDame', 'YvonneNewMalden', 'JuliaRaeBrown', 'karlturnerMP', 'DianaJohnsonMP', 'theholyllama', 'EmmaHardyMP', 'LibDemLinda', 'rachellstorer', 'Sally_Benton', 'clairemcilvenna', 'mikejwood', 'anneliese_midge', 'katetipton', 'JBuckleyMLA', 'RobbieButlerMLA', 'SorchaEastwood', 'GreenPartyJack', 'Matt_Severn', 'catsmithmp', 'alexsobel', 'richardburgon', 'CllrSamFirth', 'GaryBusuttil', 'FabianLeedsNE', 'LouiseMJennings', 'BobBuxtonYorksP', 'RykDownes', 'KatieJWhite', 'hilarybennmp', 'edleeds', 'WhetstoneSDP', 'GreensMorley', 'LibDemFox', 'NigelPe20474539', 'MarkJSewards', 'AmjadmBashir', 'rachelreevesmp', 'RajeshAgrawal', 'Zuffar_Haq', 'ShivaniRaja_LE', 'ClaudiaWebbe', 'ShockatAdam', 'jonashworth', 'CarolKibworth', 'quernstone36', 'benlibdem', 'leicesterliz', 'RNaikLC', 'Craig_A_Buckley', 'JoPlattLeigh', 'StuartThomas_LD', 'Reformukleigh', 'mariacaulfield', 'JamesMacCleary', 'DannySweeney89', 'JanetDaby', 'CJLittlemore', 'vickyfoxcroft', 'AdamPugh', 'snelling4mp', 'JoshMatthewsLD', 'elliereeves', 'ShowSloley', 'Chrissie_W13', 'CalvinBailey', 'claffertyldn', 'Mike_Fabricant', 'H_McNeillis', 'PaulRay111', 'DaveR_Lichfield', 'Hamish4Lincs', 'karlmccartney', 'LincolnReformUK', 'LindaRichWPB', 'CllrCSmalley', 'meaglemp', 'CllrSamGorst', 'JohnMHyland_', 'kimlabour1', 'RebeccaTurnerLD', 'seanhakimcad', 'DanCardenMP', 'MadeleyMartyn', 'paulabarker1', 'tommartincrone', 'robmcuk', 'IanByrneMP', 'HannahB4LiviMP', 'DebbieEwen_', 'CamiGlasgowSGP', 'caronmlindsay', 'dmclennan60', 'gregorpoynton', 'GarethReformUK', 'CharlieEvans0', 'NiaGriffithMP', 'LibDemsCarms', 'D_G_Alexander', 'ScottHam2win', 'LynJardineSNP', 'GeorgeKerevan', 'ShonaMcIn_SGP', 'JaneMHunt', 'AndyMcWilliam2', 'JeevunSandher', 'iansharpe4lboro', 'LouthHcreformuk', 'RossDPepper', 'jgslater', 'peter_aldous', 'Jess4Waveney', 'june_mummery', 'RobboRocker', 'SarahOwen_', 'EdwardGCarp', 'rach_hopkins', 'Dr_YasinRehman', 'Neil_Christian', 'SDPDickie', 'CEGPAmanda', 'Tim_Roca', 'DavidRutley', 'tania_mathias', 'JoshReynoldsSL6', 'MrsSmudge318', 'scousermoe', 'HelenGrantMP', 'stuartjeffery', 'DaveNaghiLibDem', 'Thomas_Bryer14', 'Makerfield_RFK', 'joshsimonstweet', 'WLM_LibDems', 'JWhittingdale', 'Ekua4Hulme', 'Parhamh45', 'cnorthwood', 'LucyMPowell', 'SebastianBate', 'Afzal4Gorton', 'samsterby', 'RKilpatrickMCR', 'JeffSmithetc', 'BBradley_Mans', 'PhilShieldsCllr', 'steveyemm', 'reformukmandd', 'michelledonelan', 'BrianMathew4NW', 'kerryp_labour', 'Cath_Read', 'ZafranKhan4MS', 'DrTeckKhong', 'al_mcquillan', 'sarahalan80', 'sadamsbhatti', 'CardiffW_Green', 'GeraldJonesLAB', 'fdwhitefoot', 'AlistairPembs', 'SCrabbPembs', 'TufnellHenry', 'midbedsreformuk', 'MaahwishMirza', 'HertsFarmer', 'CSibleyGreens', 'Blake_MidBeds', 'Carie4MidBucks', 'gregsmith_uk', 'GoAndrCoop', 'charlesfifield', 'cwacgreen', 'EmmaGuyReform', 'hollidb', 'gezkinsellagre1', 'FothergillKiran', 'AndyMcDonaldMP', 'SimonClarkeMP', 'JemmaDem', 'Rowaninthewoods', 'lukemyer_', 'vikki4mdnp', 'Michael4MDNP', 'AmyCallaghanSNP', 'DougallLorna', 'Alix2Win', 'LiamMckechnie2', 'Susan4_ED', 'PeterABedford', 'RossLaird55', 'kirstyjmcneill', 'OwenThompson', 'GeorgeFreemanMP', 'ashlizhaynes', 'KherKabeer', 'mrlabouruk', 'Kristy_UK', 'alisonebennett', 'DeannaMidSussex', 'DaveRowntree', 'Buchanan_dup', 'pfarrell767', 'DENISEJOHNSTO10', 'greens4mkc', 'JamesCoxLD', 'emily4mk', 'Johnny__Luk', 'chriscurtis94', 'Ben_Everitt', 'greenbuckingham', 'CllrCoxEleanor', 'JeniferGouldCH', 'drmehmoodjam', 'pippamaslin', 'Siobhain_Mc', 'Ioanbellin', 'Ian_Chandler', 'junedaviesTFP', 'DavidTCDavies', 'CatherineFookes', 'WmPowell2021', 'policy_uk', 'GlynPreston', 'elwyn04', 'craig4monty', 'Steve_Witherden', 'NeilAlexMoray', 'jrbadger29', 'EuanM_SFP', 'LizziCollinge', 'GinaDowding', 'Peter4MandL', 'davidmorrisml', 'marionfellows', 'pamela_nash', 'DonaldBoyd7', 'Torcuil', 'AngusMacNeilSNP', 'Helenceri', 'carolynharris24', 'AndrewNeath84', 'Sajidah', 'RobertJenrick', 'CollanDSiddique', 'DavidWatts12', 'DrLizochka', 'LeeRJdillon', 'Laura__Farris', 'baronstjohn', 'AnothervoiceWB', 'AJOGEE', 'Ali4Castle', 'chionwurah', 'grumpynewcastle', 'yvonneridley', 'GlindonMary', 'GreenPartyNT', 'SDPNorthEast', 'CatMcKinnell', 'jackdaviesld', 'DesmondSwayne', 'pippabartolotti', 'RachelBuckler1', 'JonathanTClark', 'LaurenJamesWGP', 'johnmiller_libd', 'jessicamordenmp', 'BrandonCymru', 'RuthNewportWest', 'peterbyrnejnr', 'JacobCousens', 'AnneMarieMorris', 'MartinWrigley', 'BrianAgar11', 'curryannemarie', 'PaulHowellMP', 'alanstrickland', 'ashton_howick', 'jon_trickett', 'antonyantoniou', 'LibDemChrisL', 'lucyrigby', 'JillHopeLibDem', 'ALewerMBE', 'mike_reader', 'Katie4MKTUSC', 'JimAllister', 'Helencmaher', 'mcguigan_philip', 'trisburnedlands', 'sianalliance', 'lucydahlia', 'PGibsonSNP', 'IanGibsonEatRaw', 'MikeMann295', 'phlipper1970', 'uday_nagaraju', 'RobynHarri28314', 'BenMaguireNC', 'scottmann4NC', 'ReformNorth', 'paulcotswolds', 'MinchChloe', 'NickyNorthDevon', 'SelaineSaxby', 'JamesColdwellUK', 'Simon4NDorset', 'lestertaylor9', 'StephenFarryMP', 'Barry_ndgreen', 'lukeakehurst', 'ReformDurham', 'cmartinLD', 'SteveBarclay', 'chalmersdavidn', 'Frankadlingtons', 'Louise_E_Jones', 'wessywes0', 'Lee4NED', 'RossShippy', 'billabowman', 'wendychambLD', 'stefanhoggan', 'alexbrewer', 'ranil', 'BradPhillipsUK', 'alexzychowski', 'SteveAZ_', 'RoystonRuth', 'vicky_burtgp', 'paulmacdonnell', 'votedannorris', 'Jacob_Rees_Mogg', 'CllrDineRomero', 'EllieChowns', 'BillWigginMP', 'Steffanaquarone', 'duncancbaker', 'cathy_cordiner', 'PatchettJa55212', 'dsnorthnorth', 'annietrev', 'baynes_simon', 'CraigGreenShrop', 'HelenMorganMP', 'Natalie_Rowley1', 'Sadik4Pharmacy', 'Ashley_Cartman', 'LiamFox', 'AlexReformUK', 'PHopkins_Reform', 'RachelTaylorNWB', 'craig4nwarks', 'sam_carling_', 'ShaileshVara', 'KemiBadenoch', 'CllrSmitaRajesh', 'issy4nwessex', 'andyfitchet', 'kitmalthouse', 'hina_tweets', 'carlbenfield', 'ABridgen', 'Hack4Labour', 'craig_smithUK', 'WestNorfolkRob', 'jamesowild', 'alicemlabour', 'Transcendental1', 'SalomonSoup', 'NickTaylor29962', 'labourlewis', 'jajo_osborn', 'DavidforNorwich', 'NadiaWhittomeMP', 'LibDem_FPL', 'AlexNorrisNN', 'LilianGreenwood', 'sutherland_cath', 'Marcus4Nuneaton', 'greennuneaton', 'louie_french', 'Juvelad', 'EJCJones93', 'debbie_abrahams', 'samlibdem', 'NickBuckleyMBE', 'ShanazSaddique', 'HannahK_LD', 'jimfromoldham', 'alexjarmitage', 'amcarmichaelMP', 'robertleslie69', 'GarethBaconMP', 'graeme_l_casey', 'ju_owens', 'JadeBotterill', 'mark4dewsbury', 'amirsteveali', 'AnnelieseDodds', 'TheoJupp', 'ChrisGoodall2', 'LaylaMoran', 'RanigaVinay', 'StephenEDWebb', 'GavNewlandsSNP', 'Alison_S_Taylor', 'granttoghill', 'JohannaBaxter', 'aqualine34', 'Miatsf', 'ShinyShep', 'AnnaFryer9', 'Jonathan_Hinder', 'Andrew4Pendle', 'miriam_cates', 'LibDemRobReiss', 'marietidball', 'JuliaLibDem', 'MCSavours', 'markjenkinsonmp', 'ReformUKPenrith', 'Amandine66eg', 'LukeGrahamUK', 'PeteWishart', 'paulbristow79', 'NicolaDay78', 'andrewpakes_', 'LibDemNick', 'S_MartinLibDem', 'JohnnyMercerUK', 'FredThomasUK', 'petergold99', 'GreenberryHolly', 'LukePollard', 'GarethBStreeter', 'yvettecooperMP', 'jamie_needle', 'olli_watkins', 'AlexDaviesJones', 'angelakaradog', 'wiliamrees', 'LeanneSpurs', 'RobertSyms', 'OliWalters93', 'Sarah_Ward50', 'ApsanaForPL', 'CllrNathalieB', 'FreddieDowning_', 'richarddflowers', 'TonyLiberator', '_Amanda_Martin_', 'PennyMordaunt', 'pompeygreens', 'Elliott000_', 'stephenmorganmp', 'Reformuk_pompey', 'Neil4Preston', 'MPHendrick', 'prestonindie', 'PutneyFleur', 'kieren', 'McEnteeFergal', 'HelenBaxter_LD', 'UK999ers', 'Georgia_Gould', 'SamiaHersi', 'VivienAviva', 'JohnHealey_MP', 'Adamwood_UK', 'ReformRayleigh', 'ChrisTaylorHock', 'DaveJMcElroy', 'MattRodda', 'henrydwright', 'livbailey', 'HelenCBelcher', 'CarolyneCulver', 'RossMackinnonWB', 'annaturley', 'JacobYoungMP', 'ChrisBloore', 'redditchrachel', 'StuartBradyLab', '_JonathanEssex', 'markjohnstonld', 'RhonddaBryant', 'rhonddaplaid', 'GeraldFrancis', 'WalesGreenParty', 'nigelmp', 'johnpotterLD', 'RishiSunak', 'feedthedrummer', 'lauracoryton', 'saragezdari', 'sarahjolney1', 'ChasWarlow', 'paulellison82', 'georgegalloway', 'andykelly', 'paulwaugh', 'GColleyLDLA', 'Dabin_ReformUK', 'LaurenREdwards', 'medwaygreens', 'KellyTolhurst', 'AndyAchilleos', 'tpc1981', 'AndrewRosindell', 'CooperGeoff', 'LabourChristie', 'carolinenokes', 'connoreshaw', 'JakeBerry', 'andymacnae', 'RUK_RossDarwen', 'SarahChampionMP', 'JakeBenRichards', 'Alex_Stafford', 'ColinDTaylor', 'rdickson4PCC', 'johnslinger', 'Jonathan_MBanks', 'tony_gill91', 'JessinRuislip', 'IPricePsychAuth', 'DSimmonds_RNP', 'MikeAmesburyMP', 'ChrisCopeman', 'JasonMoorcoft', 'robertk16', 'EllzSummary', 'NSGreenParty1', 'DrBenSpencer', 'LynnIrvingLove', 'CllrRMallender', 'jameswnaish', 'KatyLoudonSNP', 'mgshanks', 'aliciakearns', 'rmlabour', 'joewoodlabour', 'jakelibdem', 'RLong_Bailey', 'Sandhyamma', 'matt_j_aldridge', 'VCharlestonLD', 'JohnGlenUK', 'JulianMalins', 'DruidKingArthur', 'tessa1958', 'MsAlisonHume', 'RWeedenSanz', 'NicDakin55', 'NGChindam', 'damsyboi', 'Bill_Esterson', 'GLJLibDem', 'Mather_Keir', 'christianvassie', 'adhib', 'GreenLManston', 'dscottmcdonald', 'Richardfor7oaks', 'GillFurnissMP', 'SheffieldGreens', 'WillSapwell', 'MarkSheffieldWP', 'izzyafr', 'Abtisam_Mohamed', '_OliviaBlake', 'SDPhq', 'shaffaqmohd', 'AlexiDimond', 'LouHaigh', 'hannahnicklin', 'sophthor', 'SiberianT', 'Mark_Spencer', 'LeeWatersUK', 'CllrChelleWelsh', 'PhilipDaviesUK', 'annalouisedixon', 'kevinwarnes', 'jbuckleylabour', 'JulianDean99', 'alex__wagner__', 'VoteMikeBaldock', 'SwaleGreens', 'aisha_cuthbert', 'WillReformUK', 'FrancesKneller', 'kevinmckenna', 'malcolmbirks', 'VoteAndyBrown', 'ajmurday', 'JulianSmithUK', 'BJackson_Reform', 'drcarolinej', 'HanifKhan_1', 'mwinnington', 'TanDhesi', 'Jay4Sandwell', 'a_adeyemo', 'julianknight15', 'MaryMcKennaTBP', 'DrNShastriHurst', 'CulleyC58841', 'darrenpaffey', 'katherinebarb37', 'johnedwards0955', 'ThomasGravatt', 'LabourSatvir', 'JohnBlairMLA', 'PaulGirvanMP', 'DeclanKearneySF', 'roisinlynchsdlp', 'jasonreid_NI', 'RobinSwann_MLA', 'JackAFerguson', 'Metcalfe_SBET', 'ChrisChapman86', 'pippaheylings', 'Luke_Viner', 'zoe_billingham_', 'JGray', 'rozsavage', 'Lucycare', 'SamanthaNiblet4', 'HeatherWheeler', 'GreenMP4SDevon', 'AnthonyMangnal1', 'carolinevoaden', 'MattBellSDorset', 'HattonLloyd', 'DianeForsytheNI', 'ChrisHazzardSF', 'ColinSDLP', 'AndyofAlliance', 'Jim_Wells_MLA', 'MartinCCorney', 'annagelderd', 'ColinMartinPL22', 'sheryllmurray', 'BayoAlaba', 'seegreenparty', 'DavidBSampson', 'stephencummins', 'Anna_Firth', 'SEEGreenParty', 'BambosMP', 'CllrGunawardena', 'EricSJS', 'paulhilliar', 'AlbertoCostaMP', 'PMHartshorn', 'mikejelfs', 'rwparkinson', 'chrisj_brown', 'BenGoldsborough', 'catherinerowett', 'PoppySimister', 'rufiaashraf', 'ianamccord', 'HalsallSean', 'patrick_hurley', 'K_Fletcher_MP', 'SRLabourLeader', 'AngeTurner816', 'dfrancisgreen', 'EmmaLewellBuck', '_AndersonStuart', 'MatthewGreen02', 'MichaelGuest5', 'simontthomson', 'tombartleetld', 'emmabishton', 'Cllr_Carter', 'SuffolkReform', 'CllrBrazil', 'georgianelson01', 'SWDevonRebecca', 'gaganmohindra', 'NarinderSianGP', 'AlexSufit', 'SallySymington', 'swnorfolk2024', 'doctorpallavi', 'CllrTerryJermy', 'Josie_Ratcliffe', 'trussliz', 'evenor23', 'AWMurrison', 'fwhit_field', 'SunburyUk', 'claire_tigher', 'AdamGregg', 'kimleadbeater', 'SpenValleyRefUK', 'theodoraclarke', 'AVGStafford', 'StaffMoorTories', 'libdemdaisy', 'SimonGrover', 'StewartSatterly', 'stalbansspencer', 'PhilChadwick81', 'DwanJamie', 'HaleyHodgetts', 'BrexitKaya', 'JreynoldsMP', 'stevedouble', 'JoannaKenny10', 'NoahLaw4StAN', 'aapennington', 'kevinbonavia', 'stevenagelisa', 'DavidBainesStH', 'patmoloney', 'Mal_Webster', 'MarieRimmer', 'neilbenny', 'chriswkane', 'AlynSmith', 'shinergise', 'AndrewGeorge_', 'DerekThomasUK', 'AnthonyBrowneMP', 'borofergie', 'MariannaMasters', 'IanSollom', 'Wendy4Stockport', 'Helena_Dugdale', 'NavPMishra', 'LU_stockport', 'johnmacreformuk', 'Chris4SN', 'StocktonWest', 'Mattivic', 'adam_colclougha', 'NavidKaleem', 'gareth_snell', 'JoshHarris431', 'david4lcs', 'ToryPressMids', 'allisoncgardner', 'alsandiford87', 'BramhamAlex', 'HarperWallis', 'GavinWilliamson', 'ChrisBramall', 'catecclesstour', 'MrLogicUK', 'Q66Suzi', 'MichelleGuy4', 'Willpolland1', 'JimShannonMP', 'ards_richard', 'NizamAliMP', 'joehudsonsmall', 'halimanyomi', 'Uma_Kumaran', 'rubanga_a', 'JaneyisLittle', 'Crocker4Brexit', 'MP4Stratford', 'GreenPartyScott', 'ClaireBonham', 'stevereedmp', 'DJerrome', 'JamesNe84400310', 'AndrewHWestern', 'Siobhan_Baillie', 'georgejamesLD', 'PeteKennedy', 'simonforStroud', 'theresecoffey', 'JulesEwartSuff', 'Jenny4SuffCoast', 'LewisAtkinson', 'ReformUKSun', 'RachelFeather10', 'NiallHodson', 'AlPinkerton', 'StephenGanderDP', 'Nus_Ghani', 'twdrummond', 'Chrishni_Reshe', 'mark_hoath', 'AndrewmitchMP', 'RobPocock1', 'johnsweeneyroar', 'MikeEOCarroll', 'tj_sutcliffe', 'Gwyn_SW', 'andybentley1965', 'WStone4SN', 'JustinTomlinson', 'Heidi_Labour', 'RobertBuckland', 'MattMcCabe2', 'Ian4Tamworth', 'SarahEdwardsTam', 'Sue4Dodderhill', 'EddieHughes4WN', 'RyanJudeGreen', 'EstherMcVey1', 'JonathanSmithLD', 'GideonJAmos', 'ReformTaunton', 'pow_rebecca', 'trower_green', 'Green4Telford', 'ReformUKTelford', 'cllrshaundavies', 'DamolaAni', 'CateCodyEco', 'lrobertsonTewks', 'LibDemCam', 'PatmccarthyPat', 'MPritchardUK', 'RohYakobi', 'lisabanes_', 'kevinhollinrake', 'stevemason2111', 'bigandyuk1', 'LukeHall', 'greenalexjf', 'roblogan3', 'ClaireforTAY', 'MichaelBukola', 'thurrockjen', 'JackieDP', 'Shaun4WBW', 'antoniabance', 'CllrMYHussain', 'JonnyBarter92', 'RachelGilmourLD', 'Lewiswjbailey', 'TomTugendhat', 'DrRosena', 'EthanKFBrooks', 'NickHGreen', 'cllrsdarling', 'kevin_j_foster', 'CWongsosaputro', 'phildavies1995', 'nathan_edmunds', 'MatthewTorfaen', 'libdembrend', 'NickTorfaen', 'Geoffrey_Cox', 'philhutty', 'judymaciejowska', 'AlanR555', 'IsabelSaxbyUK', 'DavidLammy', 'karenlaborde', 'ruthgripper', 'jaynekirkham4', 'thisischerilyn', 'ThreshedThought', 'labour_sherwood', 'cllrtombruce', 'munirawilson', 'JohnApplebyLD', 'Lewis4Tynemouth', 'alancampbellMP', 'greenpartynt', 'carlalockhart', 'CatSeeley', 'EoinTennyson', 'DannyBeales', 'SGardnerSDP', 'IanHawkes82', 'tuckwell_steve', 'AlunCairns', 'StuartField18', 'ianjamesjohnson', 'GreenPartyBarry', 'KanishkaNarayan', 'StevenRajam', 'ReformUK_VoG', 'SouthwarkGP', 'FloEshalomi', 'ChrisD_French', 'AartiJo5hi', 'simonlightwood', 'Realkeithmason', 'AshRouth', 'LibDemVicks', 'angelaeagle', 'Turnershbo', 'Valerie_VazMP', 'reform_walsall', 'stellacreasy', 'NancyTaaffe', 'RTaylor_LibDem', 'crockett58', 'UKWarringt83170', 'charlotte2153', 'maddison4greens', 'Sarah_Hall81', 'LouisWMAdam', 'MattWestern_', 'cllrHema', 'chantkowski', 'Pdonaghyreform', 'SharonHodgsonMP', 'mozdog94', 'ReformukW', 'dean4watford', 'ianstotesbury', 'Turmaine', 'ReformUKWaveney', 'AdrianRamsay', 'RichardRout', 'MayaSeverynSDP', 'LennyRolles', 'benhabib6', 'GVKitchen', 'townsendchris', 'helenhims', 'tessamunt', 'Andrew_Lewin_', 'JohnPeterMunro', 'grantshapps', 'c_l_blake', 'AndrewBowie_MP', 'SarahCoombesWB', 'WillGoodhand4MP', 'chrisloder', 'EdwardMorelloWD', 'MartinJDocherty', 'Labour_Douglas', 'AndrewJMuir', 'RoyalDocksRob', 'SophiaNaqvi1', 'AshleyDalton_MP', 'WestLancsReform', 'MikePrendUK', 'timfarron', 'JackmanMatty', 'WLReformUK', 'DanAldridgeWsM', 'CllrThomasDaw', 'keatingpatrick', 'JohnPenroseNews', 'HenryBatchelor1', 'RebeccaDenness', 'markereiraguyer', 'NJ_Timothy', 'MatthewBellUUP', 'SteveDonnelly95', 'hbaldwin', 'PershoreDan', 'Kashifharoon', 'NMcGreenParty', 'JPYorkshireman', 'JamesMonaghan', 'AlecShelbrooke', 'andyj1979', 'dave_surtees', 'davecoveney', 'DerekTwiggMP', 'Jliffe', 'janeyfl1', 'lisanandy', 'rachelgreensw19', 'reformwimbledon', 'dunfieldprayero', 'PaulKohlerSW19', 'aaron_mafi', 'eleanorSW19', 'DannyVet', 'hannahl_dawson', 'buckley4windsor', 'pavitarmann', 'jackmrankin', 'julian_tisi', 'pagaris', 'matthew_patrick', 'JamesAbbott2013', 'tim_blaxill', 'pritipatel', 'robertcourts', 'Barry__Ingleton', 'MsGrgaMeadows', 'approsser', 'Ese_Journo', 'WillForster', 'JonathanLord', 'monhamidi', 'Sureena4WNE', 'Jane_Stevenson_', 'PeterThornton10', 'drpauldarke', 'patmcfaddenmp', 'CeliaHibbert', 'WarinderSJuss', 'Mbayliss14', 'tomcollinsworcs', 'DeVincenzo30571', 'MJWheeler85', 'PBottomleyMP', 'BeccyCooper4Lab', 'SonyaMallin', 'DodmanCharles', 'asranger', 'wxmcslibdems', 'CllrKhalilAhmed', 'SteveBakerHW', 'ToniBrodelle', 'EdmundGemmell', 'ajazrehman3', 'EmmaforWycombe', 'Mark4WyreForest', 'MelHorrocks19', 'MikeKaneMP', 'SimonLeporiLD', 'Adamjamesdance', 'MarcusFysh', 'beckymontacute', 'LeenaSFarhat', 'MSYnysMon', 'ieuan_williams_', 'GreenerLars', 'RachaelMaskell', 'lukejcr', 'AndyHollyer', 'JulianSturdy'];
  const mps = ['SarahAthertonMP', 'AndrewmitchMP', 'Bob4Beckenham', 'OfKawczynski', 'RichardFoordLD', 'JillMortimer4HP', 'UK_FoRBEnvoy', 'SarahGreenLD', 'kimleadbeater', 'MPGlosOffice', 'allandoransMP', 'AdamHollowayMP', 'Matt_VickersMP', 'Gibbo4Darlo', 'twocitiesnickie', 'SarBritcliffeMP', 'Dines4Dales', 'RobinMillarMP', 'david4wantage', 'SallyAnn1066', 'KateOsborneMP', 'GlindonMary', 'dean4watford', 'Bren4Bassetlaw', 'ApsanaBegumMP', 'JamesSunderl', 'marcolonghi4dn', 'OliverDowden', 'RishiSunak', '_RobbieMoore', 'Christian4BuryS', 'AnthonyBrowneMP', 'CharlesWalkerMP', 'DrNeilHudson', 'MPIainDS', 'PaulaBarkerMP', 'RuthNewportWest', 'maggie_erewash', 'MickWhitleyMP', 'SirRogerGale', 'ShaileshVara', 'KimJohnsonMP', 'BBradley_Mans', 'Jane_Stevenson_', 'TeamRanil', 'AndrewBowie_MP', 'YasinForBedford', 'Jacob_Rees_Mogg', 'BrineMinister', 'NavPMishra', 'Jamie4North', 'lia_nici', 'robertlargan', 'AnthonyMangnal1', 'redditchrachel', 'DanCardenMP', 'FabianLeedsNE', 'JuliaLopezMP', 'EddieHughes4WN', 'LizTwistMP', 'david_duguid', 'AJRichardsonMP', 'paulscullymp', 'TaiwoOwatemi', 'drcarolinej', 'EstherMcVey1', 'michaelgove', 'theresa_may', 'ScottBentonMP', '_AndersonStuart', 'IoWBobSeely', 'KwasiKwarteng', 'NickFletcherMP', 'GillFurnissMP', 'GarethBaconMP', 'garystreeterSWD', 'DominicRaab', 'LukeHall', 'sarahjolney1', 'ASollowayUK', 'HelenMorganMP', 'JamieWallisMP', 'JimShannonMP', 'KemiBadenoch', 'lucyfrazermp', 'baynes_simon', 'antony_hig', 'nadams', 'StevenBonnarSNP', 'ALewerMBE', 'edwardtimpson', 'DerekThomasUK', 'Laura__Farris', 'MelJStride', 'BorisJohnson', 'Chris_EvansMP', 'NickTorfaen', 'zarahsultana', 'JohnMcNallySNP', 'NickGibbUK', 'eleanor4epping', 'khalid4PB', 'PGibsonSNP', 'PeterGrantMP', 'Simon4NDorset', 'AlanBrownSNP', 'AlbertoCostaMP', 'MargaretFerrier', 'GradySNP', 'justinmadders', 'GillianKeegan', 'MickeyBradySF', 'HannahB4LiviMP', 'JohnCryerMP', 'Imran_HussainMP', 'eastantrimmp', 'BrendanOHaraMP', 'Dr_PhilippaW', 'CMonaghanSNP', 'HuwMerriman', 'Douglas4Moray', 'BethWinterMP', 'Rehman_Chishti', 'VictoriaPrentis', 'Jochurchill_MP', 'ToniaAntoniazzi', 'KieranMullanUK', 'DrLisaCameronMP', 'DavidDavisMP', 'lrobertsonTewks', 'DrBenSpencer', 'JonathanLord', 'wendychambLD', 'jcartlidgemp', 'kirstenoswald', 'KirstySNP', 'alancampbellmp', 'joannaccherry', 'PutneyFleur', 'RosieDuffield1', 'DarrenG_Henry', 'Keir_Starmer', 'carolynharris24', 'JacobYoungMP', 'DrRosena', 'MarieRimmer', 'LSRPlaid', 'AnumSNP', 'MrJohnNicolson', 'RobertJenrick', 'K_Fletcher_MP', 'MarkTamiMP', 'neill_bob', 'DerekTwiggMP', 'RicHolden', 'ChrisLawSNP', 'RobertSyms', 'TomTugendhat', 'RThomsonMP', 'AlanMakMP', 'WalkerWorcester', 'MPGeorgeEustice', 'TanDhesi', 'marykfoy', 'AlokSharma_RDG', 'SuellaBraverman', 'SimonClarkeMP', 'MarcusFysh', 'Dunne4Ludlow', 'DesmondSwayne', 'William_Wragg', 'Nus_Ghani', 'lynbrownmp', 'Marcus4Nuneaton', 'Q66Suzi', 'MGreenwoodWW', 'Simonhartmp', 'JamesDalyMP', 'Anna_Firth', 'VotePursglove', 'AlexChalkChelt', 'PaulGirvanMP', 'Rees4Neath', 'andreajenkyns', 'craig4monty', 'LabourSJ', 'nicolafrichards', 'JoStevensLabour', 'Ianblackford_MP', 'CGreenUK', 'MpHendrick', 'julianknight15', 'Lee4NED', 'louie_french', 'EdwardJDavey', 'DSimmonds_RNP', 'mark4dewsbury', 'NatalieElphicke', 'JanetDaby', 'JackLopresti', 'MaryRobinson01', 'FrancieMolloy', 'nigelmills', '_OliviaBlake', 'rach_hopkins', 'SarahChampionMP', 'AndyMcDonaldMP', 'Peter_Dowd', 'HenrySmithUK', 'PeterBoneUK', 'MartinVickers', 'MariaMillerUK', 'KevanJonesMP', 'morton_wendy', 'SCrabbPembs', 'AJonesMP', 'BobBlackman', 'MPritchardUK', 'JulieElliottMP', 'AWMurrison', 'EmmaLewellBuck', 'JulianSmithUK', 'SKinnock', 'RupaHuq', 'IanMearnsMP', 'SDoughtyMP', 'PreetKGillMP', 'LindsayHoyle_MP', 'Caroline_Ansell', 'DavidRutley', 'CWhittaker_MP', 'StephenFarryMP', 'Siobhain_Mc', 'PaulHowellMP', 'NadiaWhittomeMP', 'IanByrneMP', 'richardbaconmp', 'HuddlestonNigel', 'Y_FovargueMP', 'LeoDochertyUK', 'DavidTCDavies', 'RichardBurgon', 'joymorrissey', 'BlaenauGwentMP', 'LiamFox', 'AnnelieseDodds', 'RebeccaHarrisMP', 'JonCruddas_1', 'BillWigginMP', 'GeraldJonesLAB', 'StephenFlynnSNP', 'karinsmyth', 'Tobias_Ellwood', 'NiaGriffithMP', 'drlukeevans', 'EdwardLeighMP', 'Shaun4WBW', 'PennyMordaunt', 'NadineDorries', 'BenMLake', 'DanielZeichner', 'JSHeappey', 'CSkidmoreUK', 'Metcalfe_SBET', 'KarlTurnerMP', 'bhatti_saqib', 'Mark_J_Harper', 'DeidreBrock', 'DamianGreen', 'KateOsamor', 'WayneDavid_MP', 'hilarybennmp', 'ShabanaMahmood', 'OrfhlaithBegley', 'JudithCummins', 'AmyCallaghanSNP', 'DaveDooganSNP', 'munirawilson', 'SMcPartland', 'CliveEfford', 'alanwhiteheadmp', 'AngelaCrawley30', 'ConorBurnsUK', 'NorwichChloe', 'RLong_Bailey', 'cj_dinenage', 'HollyLynch5', 'amandamilling', 'PaulBlomfieldMP', 'JohnHealey_MP', 'GarySambrook89', 'pow_rebecca', 'JeromeMayhew', 'tomhunt1988', 'GavinWilliamson', 'thisischerilyn', 'NazShahBfd', 'CatherineWest1', 'GarethDavies_MP', 'abenaopp', 'ChrisHazzardSF', 'charlotte2153', 'ClaireCoutinho', 'KeeleyMP', 'YvetteCooperMP', 'Valerie_VazMP', 'BimAfolami', 'ABridgen', 'TahirAliMP', 'IanLaveryMP', 'RobBAylesbury', 'Meg_HillierMP', 'danny__kruger', 'TommySheppard', 'ElliotColburn', 'J_Donaldson_MP', 'PeteWishart', 'AndrewHWestern', 'jamesowild', 'SteveBarclay', 'SelaineSaxby', 'ThangamMP', 'helenhayes_', 'KarenPBuckMP', 'peter_aldous', 'johnfinucane', 'drewhendrySNP', 'DougChapmanSNP', 'SarahOwen_', 'JustinTomlinson', 'BarrySheerman', 'GRobinsonDUP', 'coyleneil', 'rushanaraali', 'ChrisStephens', 'MattWestern_', 'AaronBell4NUL', 'KennyMacAskill', 'DanJarvisMP', 'BellRibeiroAddy', 'mimsdavies', 'Offord4Hendon', 'Debbie_abrahams', 'GregClarkMP', 'bernardjenkin', 'AngelaRayner', 'John4Carlisle', 'Alex_Stafford', 'GarethThomasMP', 'StewartHosieSNP', 'KellyTolhurst', 'JakeBerry', 'MattRodda', 'simonjamesjupp', 'Stuart_McDonald', 'JNHanvey', 'carolinenokes', 'mariacaulfield', 'OliverHealdUK', 'Afzal4Gorton', 'SharonHodgsonMP', 'Michael4MDNP', 'chrisloder', 'gregsmith_uk', 'meaglemp', 'jon_trickett', 'Kate_HollernMP', 'MarshadeCordova', 'davidmorrisml', 'cmackinlay', 'jamesmurray_ldn', 'vickyfoxcroft', 'pauljholmes', 'CPJElmore', 'SamanthaDixonMP', 'ChrisPincher', 'EmilyThornberry', 'JohnPenroseNews', 'JamesMorris', 'Mark_Spencer', 'JimfromOldham', 'HackneyAbbott', 'GeraintDaviesMP', 'ACunninghamMP', 'LouHaigh', 'BWallaceMP', 'GuyOpperman', 'JonAshworth', 'GavNewlandsSNP', 'craig4nwarks', 'griffitha', 'JonesyFay', 'PauletteHamilto', 'ronniecowan', 'Andrew4Pendle', 'Tom_Randall', 'JDjanogly', 'Helen_Whately', 'John2Win', 'AlecShelbrooke', 'Siobhan_Baillie', 'JWhittingdale', 'gildernewm', 'PhilipDaviesUK', 'GregHands', 'angelaeagle', 'JamesDuddridge', 'nadhimzahawi', 'Bill_Esterson', 'MhairiBlack', 'Ben_Everitt', 'jeremycorbyn', 'michelledonelan', 'alisonthewliss', 'markjenkinsonmp', 'DawnButlerBrent', 'TulipSiddiq', 'libdemdaisy', 'scottmann4NC', 'Jeremy_Hunt', 'margarethodge', 'PBottomleyMP', 'RuthCadbury', 'timloughton', 'BarryGardiner', 'leicesterliz', 'Geoffrey_Cox', 'stephenctimms', 'BambosMP', 'GeorgeFreemanMP', 'BillCashMP', 'iainastewart', 'JohnnyMercerUK', 'ChrisClarksonMP', 'lisanandy', 'johnredwood', 'MartynDaySNP', 'amcarmichaelMP', 'AndrewSelous', 'CPhilpOfficial', 'cajardineMP', 'JGray', 'ChiOnwurah', 'AnneMarieMorris', 'chhcalling', 'PaulMaskeyMP', 'CarolineLucas', 'RachaelMaskell', 'timfarron', 'marionfellows', 'Jesse_Norman', 'IanMurrayMP', 'CatMcKinnell', 'johnmcdonnellMP', 'AlunCairns', 'CrispinBlunt', 'Royston_Smith', 'YasminQureshiMP', 'MikeKaneMP', 'DianaJohnsonMP', 'paulbristow79', 'jogideon', 'FeryalClark', 'hammersmithandy', 'trussliz', 'NeilDotObrien', 'tracey_crouch', 'Ed_Miliband', 'tobyperkinsmp', 'pritipatel', 'theodoraclarke', 'grahamemorris', 'GwynneMP', 'MarkPawsey', 'elliereeves', 'Steph_Peacock', 'ClaudiaWebbe', 'theresecoffey', 'kevinhollinrake', 'S_Hammond', 'AngusMacNeilSNP', 'kevin_j_foster', 'jessicamordenmp', 'aliciakearns', 'AshleyDalton_MP', 'lloyd_rm', 'JackieDP', 'andrealeadsom', 'GilesWatling', 'labourlewis', 'JohnGlenUK', 'ConorMcGinn', 'JaneMHunt', 'RachelReevesMP', 'AlexDaviesJones', 'LucyMPowell', 'SeemaMalhotra1', 'FelicityBuchan', 'CatSmithMP', 'simonlightwood', 'OwenThompson', 'gaganmohindra', 'DehennaDavison', 'liambyrnemp', 'karlmccartney', 'MrAndy_Carter', 'SamTarry', 'patmcfaddenmp', 'duncancbaker', 'MartinJDocherty', 'HelenGrantMP', 'BenPBradshaw', 'StephenMorganMP', 'SteveReedMP', 'tony4rochdale', 'VirendraSharma', 'LaylaMoran', 'AnneMcLaughlin', 'AlynSmith', 'carlalockhart', 'DavidLinden', 'alexburghart', 'JamesDavies', 'AdamAfriyie', 'peterkyle', 'KevinBrennanMP', 'HeatherWheeler', 'spellar', 'Alison_McGovern', 'steve_mccabe', 'HywelPlaidCymru', 'stevedouble', 'mtpennycook', 'JulieMarsonMP', 'RhonddaBryant', 'columeastwood', 'FloEshalomi', 'ClaireHanna', 'willquince', 'StuartAndrew', 'darrenpjones', 'wesstreeting', 'MikeAmesburyMP', 'robertcourts', 'annietrev', 'Mark4WyreForest', 'LilianGreenwood', 'AlexNorrisNN', 'AndrewRosindell', 'sajidjavid', 'jessphillips', 'HarrietHarman', 'Wera_Hobhouse', 'Michael_Ellis1', 'MattHancock', 'halfon4harlowMP', 'JasonMcCartney', 'StewartMcDonald', 'DavidMundellDCT', 'kitmalthouse', 'bphillipsonMP', 'hbaldwin', 'Pauline_Latham', 'Mike_Fabricant', 'JeffSmithetc', 'jreynoldsMP', 'sheryllmurray', 'KerryMP', 'DavidLammy', 'mattwarman', 'scullyp', 'DavidEvennettMP', 'DavidJonesMP', 'BrandonLewis', 'simonfell', 'lucyallan', 'alexsobel', 'stellacreasy', 'GregKnight', 'SteveBakerHW', 'PaulMaynardUK', 'DamianCollins', 'mikejwood', 'vickyford', 'AnnaMcMorrin', 'DamianHinds', 'grahamstuart', 'RobertBuckland', 'grantshapps', 'JamesCleverly', 'BrineMP', 'LukePollard', 'nigelmp', 'JulianSturdy'];
  /*
  This list comes from:
  https://developer.x.com/en/docs/twitter-api/enterprise/powertrack-api/guides/operators

  It’s mostly BCP-47, but with some idiosyncracies.
  E.g.:
    * Hebrew is `iw` instead of `he`
    * Indonesian is `in` instead of `id`
    * Haitian Creole is included (`ht`)
  */
  const langLookup = {'am': 'Amharic', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'bo': 'Tibetan', 'bs': 'Bosnian', 'ca': 'Catalan', 'ckb': 'Sorani Kurdish', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'dv': 'Maldivian', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'eu': 'Basque', 'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati', 'hi': 'Hindi', 'hi-Latn': 'Latinized Hindi', 'hr': 'Croatian', 'ht': 'Haitian Creole', 'hu': 'Hungarian', 'hy': 'Armenian', 'in': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iw': 'Hebrew', 'ja': 'Japanese', 'ka': 'Georgian', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'lo': 'Lao', 'lt': 'Lithuanian', 'lv': 'Latvian', 'ml': 'Malayalam', 'mr': 'Marathi', 'my': 'Burmese', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'or': 'Oriya', 'pa': 'Panjabi', 'pl': 'Polish', 'ps': 'Pashto', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'sr': 'Serbian', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Tagalog', 'tr': 'Turkish', 'ug': 'Uyghur', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-CN': 'Simplified Chinese', 'zh-TW': 'Traditional Chinese', 'zh': 'Chinese', 'art': 'X', 'qam': 'X', 'qct': 'X', 'qht': 'X', 'qme': 'X', 'qst': 'X', 'und': 'X', 'zxx': 'X'}

  const reasonsLookup = {1: "Factual error", 2: "Manipulated media", 3: "Missing important context", 4: "Other", 5: "Outdated information", 6: "Satire", 7: "Unverified claim as fact"}

  const getReasons = function (values) {
    if (!Array.isArray(values)) {
      return values;
    }
    return values.map(v => reasonsLookup[v]).join(", ");
  }

  const includesReason = function (reason) {
    return function (rowData, rowIdx) {
      return rowData['reasons'].includes(reason);
    }
  }

  let table = new DataTable('#notes-table', {
    layout: {
      top2Start: 'search',
      top: 'searchPanes',
      topStart: 'info',
      topEnd: 'paging',
      bottomStart: 'info',
      bottom2Start: 'pageLength'
    },
    fixedHeader: true,
    ajax: {
      url: '{{ '/data/notes.json' | relative_url }}',
      dataSrc: ''
    },
    columns: [
      {
        data: 'created_at',
        render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          return '<a href="https://twitter.com/i/birdwatch/t/' + row['tweet_id'] + '" target="_blank">' + luxon.DateTime.fromISO(data).toFormat('d MMM yyyy') + '</a>';
        },
        searchable: false
      },
      {
        data: 'shown',
        defaultContent: '',
        render: function (data, type, row, meta) {
          if (data === undefined) {
            return '';
          }
          if (type !== 'display') {
            return data;
          }
          content = luxon.DateTime.fromISO(data).toFormat('d MMM yyyy')
          if (row['removed']) {
            content += ' (since removed)';
          }
          return content;
        },
        searchable: false
      },
      {
        data: 'tweet_id',
        width: '550px',
        render: function (data, type, row, meta) {
          if (type !== 'display') {
            return data;
          }
          content = row['tweet'] ? row['tweet'] : '';
          return '<blockquote class="twitter-tweet">' + content + '<a href="https://twitter.com/_/status/' + data + '"></a></blockquote>';
        }
      },
      {
        data: 'summary'
      },
      {
        data: 'reasons',
        render: function (data, type, row, meta) {
          return getReasons(data);
        },
        searchPanes: {
          options: [
            {
              label: 'Factual error',
              value: includesReason(1),
            },
            {
              label: 'Manipulated media',
              value: includesReason(2),
            },
            {
              label: 'Missing important context',
              value: includesReason(3),
            },
            {
              label: 'Other',
              value: includesReason(4),
            },
            {
              label: 'Outdated information',
              value: includesReason(5),
            },
            {
              label: 'Satire',
              value: includesReason(6),
            },
            {
              label: 'Unverified claim as fact',
              value: includesReason(7),
            }
          ]
        }
      },
      {
        data: 'lang',
        visible: false,
        defaultContent: '',
        render: function (data, type, row, meta) {
          if (!data) {
            if (type === 'sort') {
              return '~ (put this last)';
            }
            if (type === 'display') {
              return 'Unknown language (see about page)';
            }
            return data;
          }
          const niceName = langLookup[data];
          if (niceName === 'X') {
            // there are a handful of language codes that are used for
            // esoteric twitter things, including emoji-only tweets (`art`)
            // and hashtag-only tweets (`qht`). We lump these all together
            if (type === 'display') {
              return 'Twitter special (see about page)';
            }
            return niceName;
          }
          if (type === 'display' || type === 'sort') {
            return niceName;
          }
          return data;
        }
      },
      {
        data: 'deleted',
        visible: false,
        defaultContent: 0,
        render: function (data, type, row, meta) {
          if (type === 'display') {
            return (data === 1) ? 'Deleted' : 'Published';
          }
          return data;
        }
      },
      {
        data: 'user',
        searchable: true,
        visible: false,
        defaultContent: ''
      },
      {
        data: 'tweet',
        searchable: true,
        visible: false,
        defaultContent: ''
      },
      {
        data: 'rating',
        searchable: true,
        visible: true,
        render: function (data, type, row, meta) {
          if (!data) {
            return 0;
          }
          if (type === 'display') {
            return data.toLocaleString();
          }
          return data;
        }
      },
      {
        data: 'user',
        visible: false,
        defaultContent: '',
        searchPanes: {
          options: [
            {
              label: 'GE2024 candidates',
              value: function (rowData, rowIdx) {
                return candidates.includes(rowData['user']);
              }
            },
            {
              label: 'Former UK MPs',
              value: function (rowData, rowIdx) {
                return mps.includes(rowData['user']);
              }
            }
          ]
        }
      },
    ],
    drawCallback: function (settings) {
      twttr.widgets.load();
    },
    searchPanes: {
      orderable: false,
      columns: [5, 6, 10, 4],
      preSelect: [
        {
          column: 5,
          rows: ['en', 'X', '']
        },
        {
          column: 6,
          rows: [0]
        },
      ],
      initCollapsed: true
    }
  });

  twttr.events.bind(
    'rendered',
    function () {
      table.fixedHeader.adjust();
    }
  );
</script>
