"use strict";
const COPY = {
 en: {
  "achievementMathSetupTitle":"Mathematical formulation",
  "achievementMathResultTitle":"Precise theorem / proven bounds",
  "achievementGhzExactMathNotation":"Let L be a nonzero real n-linear form on (ℝᵐ)ⁿ. Its real norm is maximized on sign vectors in {−1,1}ᵐ; the complexified norm is maximized on phase vectors in 𝕋ᵐ. The supremum also ranges over m.",
  "achievementGhzExactMathDetail":"Here vₙ is the maximal visibility at which all full planar GHZ correlations admit a local model for every finite collection of settings; ζ is the Riemann zeta function.",
  "achievementGhzThreeMathNotation":"The constant κ₃=1/v₃ comes from the same multilinear/GHZ problem. Q is the finite set of odd primes used in the K7 Bell witness; L₃ is its exact lower bound.",
  "achievementGhzThreeMathDetail":"The K7 witness establishes the lower inequality; an explicit local model yields the upper inequality. Equality at the upper endpoint is still a conjecture.",
  "achievementMixingMathNotation":"For σ-fields ℱ and 𝒢, α is the strong-mixing coefficient. The complex covariance convention is Cov(X,Y)=𝔼(XY)−(𝔼X)(𝔼Y), without conjugating Y; X and Y are measurable with respect to ℱ and 𝒢.",
  "achievementMixingMathDetail":"The constant is sharp: P04 gives equality constructions for complex unit-bounded variables. K_G(2)=√2 is the real Grothendieck constant of order two.",
  "achievementMultilinearMathNotation":"Let B be an n-linear form taking real values on real inputs. The indicator seminorm d∞(B) is measured on products of event indicators. The dependence functional Δₙ is one such form.",
  "achievementMultilinearMathDetail":"Both coefficients are sharp for forms real on real inputs. For n≥4 the complex coefficient has the explicit formula for κₙ; the exact κ₃ is still unknown.",
  "achievementCfProfileMathNotation":"Let |Zⱼ|≤1 almost surely, with prescribed rⱼ=|𝔼Zⱼ|. Write R=∏rⱼ and S=∑arccos(rⱼ), and optimize over all compatible joint laws.",
  "achievementCfProfileMathDetail":"When S≤π, the common fair-sign coupling attains the extremum. The unrestricted sharp constant C_d is the maximum of the profile over r.",
  "achievementStabilityMathNotation":"Let P be a law on the closed unit polydisk, D(P) its product-moment factorization defect, C_d its universal maximum, and Δ(P)=C_d−D(P). The equality orbit ℰ_d consists of common-sign two-point laws up to coordinate rotations.",
  "achievementStabilityMathDetail":"For the biased two-point family Pη, the deficit is quadratic in η while the p-th power of transport distance is linear. Thus the exponent 1/(2p) cannot be improved.",
  "achievementProblemTitle":"What is the question?",
  "achievementOriginTitle":"Where did the question come from?",
  "achievementImportanceTitle":"Why does it matter?",
  "achievementAnswerTitle":"What was established?",
  "achievementSourcesHeading":"Sources for this result",
  "achievementSourcesExplanation":"The CF Dependence paper is listed alongside earlier research and mathematical background. These links do not replace independent verification of the new proof.",
  "sourceRoleOur":"CF publication",
  "sourceRoleOrigin":"History of the problem",
  "sourceRolePrior":"Previous results",
  "sourceRoleBackground":"Scientific background",
  "sourceRoleProof":"Proof verification",
  "sourceRoleRelated":"Related work",
  "achievementGhzExactProblem":"How much noise can be added to the correlations of an entangled quantum state before a local classical explanation becomes possible?",
  "achievementGhzExactOrigin":"The problem grew out of Bell inequalities: Mermin studied multipartite entanglement in 1990, Żukowski introduced tests using all measurement settings in 1993, and later studies sought better bounds using numerical optimization.",
  "achievementGhzExactWhy":"The threshold tells an experimenter how much visibility must remain to rule out this particular class of classical models. An exact answer avoids choosing an arbitrary finite set of measurement angles.",
  "achievementGhzExactAnswer":"For four or more participants, P04 gives an exact formula for planar measurements in the full-correlation GHZ model. For four participants the critical visibility is 34/105 (about 32.38%).",
  "achievementGhzThreeProblem":"For three entangled particles, what is the exact smallest visibility at which all planar GHZ correlations can no longer be described by a local classical model?",
  "achievementGhzThreeOrigin":"The same Bell-test question is harder with three participants. Work published in 2023 and 2024 narrowed the answer numerically and analytically, but did not find an exact threshold.",
  "achievementGhzThreeWhy":"A narrow rigorous interval tells us how close we are to the true answer, and provides a more demanding benchmark for future constructions of local models and Bell inequalities.",
  "achievementGhzThreeAnswer":"P04 improves both ends of the 2024 interval. The lower bound comes from a Bell inequality checked by 272 exact rational tests; the upper bound comes from a constructive classical model. The proposed exact formula is still a conjecture.",
  "achievementMixingProblem":"If two groups of random quantities depend only weakly on one another, how large can the covariance of bounded complex-valued observations still be?",
  "achievementMixingOrigin":"Strong mixing measures dependence between two collections of events. Dvoretzky (1972), Bradley and Bryc (1985), and subsequent work established general covariance bounds, but earlier constants were not optimal.",
  "achievementMixingWhy":"The smallest possible coefficient turns a qualitative claim of weak dependence into a precise guaranteed error bound, useful when studying dependent data and stochastic processes.",
  "achievementMixingAnswer":"P04 proves a sharp constant of 4√2 for bounded complex observations under the stated strong-mixing normalization. For bounded real observations, the sharp constant is 4.",
  "achievementMultilinearProblem":"With three or more dependent groups, how large can a joint multilinear interaction be compared with a measure of their dependence?",
  "achievementMultilinearOrigin":"In 1985 Bradley and Bryc proved general inequalities but explicitly noted that their coefficients were not sharp. Finding best constants connects probability to multilinear analysis and Bell-correlation geometry.",
  "achievementMultilinearWhy":"Better constants reveal the actual extreme behavior of interactions and prevent bounds that overstate how much dependence may accumulate across several groups.",
  "achievementMultilinearAnswer":"P04 determines the sharp real and complex factors for forms that are real-valued on real inputs; for n≥4 the complex factor has an explicit zeta-function expression. This does not settle the original 1985 problem for all complex multilinear forms.",
  "achievementCfProfileProblem":"How far can a joint probability law deviate from independence when the size of each component's mean is already fixed?",
  "achievementCfProfileOrigin":"Independence makes the joint characteristic function equal the product of its marginal characteristic functions. Characteristic-function tests have been studied for decades; more recent work defines dependence measures directly from this difference.",
  "achievementCfProfileWhy":"The largest possible discrepancy tells us the natural scale of such a dependence measure. Without it, a reported value is hard to interpret or compare across dimensions.",
  "achievementCfProfileAnswer":"P01 gives the exact extremal value as a formula involving only the prescribed mean moduli. The universal constants include C₃=2/√3 and C₄=9/7, with explicit equality constructions.",
  "achievementStabilityProblem":"When a joint law comes close to the largest possible dependence value, must its structure also be close to a law that reaches the maximum?",
  "achievementStabilityOrigin":"Exact inequalities identify the ceiling, but say nothing about almost-maximizing cases. Stability theory and optimal transport supply ways to measure distance to the equality cases.",
  "achievementStabilityWhy":"Real-world distributions rarely achieve a theoretical maximum exactly. Stability answers how confidently a nearly optimal numerical value reveals the underlying extremal structure.",
  "achievementStabilityAnswer":"For d≥3 and any finite p≥1, P13 bounds the Wasserstein distance to the full family of maximizers by a constant times Δ^(1/(2p)) for sufficiently small deficit Δ. The exponent cannot be improved.",
  "achievementNav":"Achievements",
  "achievementHighlightLabel":"SELECTED RESULTS",
  "achievementHighlightHeading":"Major research achievements",
  "achievementHighlightIntro":"Four results explained in detail on a separate page, with background and 6–7 sources for each.",
  "achievementHighlight1Name":"Exact GHZ noise threshold for four or more particles",
  "achievementHighlight1Text":"The exact threshold for the specified quantum correlations is 34/105 with four particles.",
  "achievementHighlight2Name":"Three-particle GHZ: an extremely narrow remaining interval",
  "achievementHighlight2Text":"Both ends improve on earlier work, but the proposed exact formula containing ζ(3) remains open.",
  "achievementHighlight3Name":"Weak dependence: a sharp covariance bound",
  "achievementHighlight3Text":"The best coefficient 4√2 improves the earlier value 2π for bounded complex observations.",
  "achievementHighlight4Name":"How large can dependence become?",
  "achievementHighlight4Text":"P01 gives an exact formula and sharp constants, including C₃=2/√3 and C₄=9/7.",
  "achievementHighlightCTA":"See the results and their sources →",
  "achievementCaution":"Exact mathematical results and improvements in still-open problems are identified separately. External proof and priority reviews have not yet been completed.",
  "achievementBack":"← Overview",
  "achievementCatalogue":"All papers",
  "achievementPageEyebrow":"SELECTED SCIENTIFIC RESULTS",
  "achievementPageHeading":"Research achievements",
  "achievementPageLead":"Six mathematical results explained without unnecessary jargon: the question, its history, why it matters and what we know.",
  "achievementContextTitle":"What these claims mean",
  "achievementContextText":"First we explain each question and its background. Then we show the mathematical result and the sources. Proven formulas, partial improvements and conjectures are clearly distinguished; independent reviews are still pending.",
  "achievementTocGhzExact":"GHZ: exact n≥4",
  "achievementTocGhzThree":"GHZ: three parties",
  "achievementTocMixing":"Sharp covariance",
  "achievementTocMultilinear":"1985 multilinear question",
  "achievementTocProfile":"Universal CF profile",
  "achievementTocStability":"Sharp stability",
  "achievementStateExact":"Exact under stated assumptions",
  "achievementStatePartial":"Narrowed bounds; problem still open",
  "achievementStateRestricted":"Partial answer; general problem open",
  "achievementGhzExactTitle":"Exact planar GHZ threshold for n ≥ 4",
  "achievementGhzExactDescription":"The paper derives a closed formula for the optimal local-hidden-variable threshold in the planar XY, full-correlation GHZ scenario, allowing arbitrary finite sets of measurement angles.",
  "achievementExample":"Example",
  "achievementGhzExactImportance":"Previous studies gave rigorous bounds for selected measurement schemes. The new formula addresses the full planar full-correlation setting, rather than only one finite choice of angles.",
  "achievementGhzExactScope":"This concerns planar XY measurements and full GHZ correlations. It does not cover every Bell test or arbitrary measurements. Independent mathematical and historical reviews are still needed.",
  "achievementReadP04":"P04 — published series (Zenodo) ↗",
  "achievementReadDvp":"Designolle–Vértesi–Pokutta (2024) ↗",
  "achievementGhzThreeTitle":"Three-party GHZ: a narrow interval and an exact-value conjecture",
  "achievementGhzThreeDescription":"For three parties the sharp value is not yet proved. The published paper provides a new finite-harmonic Bell lower bound and an analytical upper bound from an explicit square-wave/Möbius local model.",
  "achievementGhzThreeComparison":"The 2024 visibility interval was 0.49129–0.49143. P04 improves both ends. The remaining interval for κ₃ is only about 0.01775% of its upper bound.",
  "achievementGhzThreeConjecture":"The proposed exact value is κ₃ = 105ζ(3)/(2π³). This equality has not been proved.",
  "achievementGhzThreeProof":"The lower bound uses an analytic argument and 272 precisely specified rational checks (the K7 certificate). The verification is reproducible, but it has not received independent external proof review.",
  "achievementGhzThreeZeta":"Why is the exact answer difficult? Oscillations involving the Möbius function and zeros of the zeta function obstruct a natural construction of a Bell inequality. This is not equivalent to the Riemann hypothesis.",
  "achievementMixingTitle":"Optimal covariance constant under strong mixing",
  "achievementMixingDescription":"For bounded complex random variables measurable with respect to two σ-fields, P04 establishes the sharp coefficient in the covariance inequality with the classical strong-mixing coefficient α.",
  "achievementMixingHistory":"Dvoretzky's earlier factor was 2π (about 6.28). P04 obtains the smaller, sharp factor 4√2 (about 5.66). For real observations, the sharp factor is 4.",
  "achievementMixingScope":"Both comparisons use the same definition of strong mixing and the same normalization. A separate literature check is still needed before claiming world priority.",
  "achievementReadBradley":"Bradley–Bryc (1985) ↗",
  "achievementMultilinearTitle":"Sharper multilinear estimates and the question from 1985",
  "achievementMultilinearDescription":"Bradley and Bryc observed in 1985 that their general multilinear coefficients were not optimal. P04 derives sharp real and complex factors 2ⁿ and 2ⁿκₙ for a natural class of multilinear forms real-valued on real arguments.",
  "achievementMultilinearScope":"The 1985 question covers all complex multilinear forms. P04 proves a sharp answer for a narrower, natural subclass. The general question, and the exact complex value at n=3, remain open.",
  "achievementProfileTitle":"Universal characteristic-function dependence profile",
  "achievementProfileDescription":"An extremum over joint laws of bounded complex random variables is reduced to a formula in the prescribed moduli of their means. This unifies several characteristic-function factorization problems.",
  "achievementProfileImportance":"For example, C₂=1, C₃=2/√3 and C₄=9/7. There are explicit distributions attaining the bounds, and C_d increases to 2. We do not claim this resolves an independently identified old open problem.",
  "achievementReadP01":"P01 — published series (Zenodo) ↗",
  "achievementStabilityTitle":"Sharp quantitative stability near extremal dependence",
  "achievementStabilityDescription":"P13 strengthens the sharp inequality into a stability theorem: if the dependence defect is close to its maximum, the joint distribution must be close to the entire family of equality cases.",
  "achievementStabilityScope":"For d≥3, finite p≥1 and sufficiently small deficit Δ, the exponent 1/(2p) is optimal. A different, more structured measure of deviation has a sharp square-root rate.",
  "achievementStabilityPriority":"This is a sharp mathematical theorem. It has not been independently classified as a solution to a historically posed open question.",
  "achievementReadP13":"P13 — published series (Zenodo) ↗",
  "achievementEditorialTitle":"Proof, novelty and priority",
  "achievementEditorialText":"Each achievement has its own 6–7 sources: the CF paper, earlier results and background references. These explain the development of the question; they are not independent verification of our proofs.",
  "achievementEditorialSecond":"The exact three-party GHZ formula is still a conjecture. The broader complex multilinear question from 1985 is also not settled. Neither is advertised as fully solved.",
  "achievementAllPapers":"Explore all published papers →",
  papers:"Publications",updates:"What's new",about:"About",eyebrow:"EXTREMAL PROBABILITY · ANALYSIS · ALGEBRA",
  hero:"A research programme on dependence via characteristic functions, sharp inequalities, and the mathematical structures behind their extremizers.",
  programmeLabel:"THE SCIENTIFIC PROGRAMME",programmeHeading:"What CF Dependence studies",
  programmeLead:"The programme originated in characteristic-function measures of dependence and now investigates mathematical interactions through their observations, constraints and extremal properties.",
  programmeObjectHeading:"Research object",
  programmeObject:"For a joint probability law P with marginals P₁, …, P_d, the central object is the signed interaction measure: the difference between the joint law and the product of its marginals.",
  programmeObjectNote:"The Fourier factorization defect is the original observable—not the boundary of the project. Other norms, harmonic representations, transport and interaction observables open different extremal questions.",
  programmeGoalHeading:"Research goal",
  programmeGoal:"Discover new mathematical laws, prove them analytically where possible, and identify common mechanisms that explain entire classes of results rather than isolated examples.",
  programmeMethodHeading:"How the project works",
  programmeMethod:"Explore examples, numerical experiments and counterexamples; extract invariants and essential coordinates; formulate an explicit law, prove it rigorously and test whether the mechanism transfers to other problems. Exact bounds, extremizers, equality and stability are central questions.",
  programmeBridge:"The subject-organized publications above show how this programme develops sharp inequalities, prescribed marginals and transport, algebra, inverse harmonic methods and statistics.",
  areasNav:"By field",areasLabel:"RESEARCH MAP",areasHeading:"Publications by research area",
  keyResultsHeading:"Key results",resultsLabel:"Key results",
  resultsFromVersion:"Results described from published version",areasIntro:"An annotated scientific guide: each published article has a short overview and three selected results from its verified text.",
  areasUnavailable:"The publication catalogue could not be displayed. Reload this page and try again.",
  firstPublished:"First publication",lastChanged:"Latest published revision",
  latestVersionNumber:"Latest version",unknownVersion:"Version not verified",zenodoOrdinal:"Zenodo release",
  publicationDateNote:"Dates refer to published Zenodo versions, not edits of this website.",
  verifiedAsOf:"Catalogue curated on",zenodoUpdated:"Public Zenodo metadata refreshed on",missingDate:"Date not independently verified",releaseDate:"Publication date",
  versionIdentifier:"Verified version DOI",openLatest:"Open latest version",
  latestPublished:"Latest published record (Concept DOI)",lastVerifiedDate:"Last verified release date",
  verifiedVersionDOI:"Last verified version DOI (for citation)",
  doiExplanation:"Dates refer to the first and latest published Zenodo releases, not website edits. The concept DOI follows the latest version; the version DOI fixes one release.",
  olderPdf:"Archived PDF",olderTex:"Archived TeX",zenodoPDF:"PDF on Zenodo",
  publishedLabel:"PUBLISHED RESEARCH",papersHeading:"Research papers",publishedCount:"published records",
  searchLabel:"Search publications",noMatches:"No publications match your search.",
  newsLabel:"PROJECT UPDATES",updatesHeading:"What's new",
  updatesInfo:"Verified website improvements and published research releases, in reverse chronological order.",
  siteUpdateKind:"Website update",publicationUpdateKind:"Publication",
  olderUpdatesLabel:"Earlier updates",
  staticUpdateP19Title:"P19: dependence synthesis with prescribed marginals",
  staticUpdateP19Text:"New preprint: joint distributions under moment, spectral-zero and Fourier constraints.",
  staticUpdateP20Title:"P20: statistical estimation of extremal dependence",
  staticUpdateP20Text:"New preprint: growing frequency profiles, random frequency banks and Walsh calibration.",
  staticUpdateCollectionTitle:"CF V6: fifteen new research papers added",
  staticUpdateCollectionText:"The public catalogue expands from three to eighteen research papers.",
  staticUpdateInitialTitle:"Initial public manuscript collection",
  staticUpdateInitialText:"Three first research manuscripts (P01–P03) published in the public repository.",
  staticUpdateMathTitle:"Detailed mathematical formulations added",
  staticUpdateMathText:"Definitions, hypotheses and precise formulas were added to all six achievements, and four concise formulas now appear on the homepage.",
  staticUpdateSourcesTitle:"Results explained with separate references",
  staticUpdateSourcesText:"Each achievement now explains its problem, history, importance and mathematical result, with 6–7 sources specific to that result.",
  authorNav:"Author",authorLabel:"RESEARCHER",authorHeading:"About the author",
  authorRole:"Independent Researcher",
  aiDisclosureLabel:"RESEARCH TRANSPARENCY",aiDisclosureHeading:"AI collaboration disclosure",
  aiDisclosureText:"CF Dependence research was conducted by the author in collaboration with artificial intelligence (AI) systems. AI assisted with mathematical exploration, developing and critically examining ideas and proofs, and preparing manuscripts. AI systems are not listed as co-authors. The author is responsible for the published mathematical statements, proofs, and conclusions.",
  aboutLabel:"RESEARCH AREAS & PUBLICATIONS",aboutHeading:"About CF Dependence",
  aboutText:"Five connected mathematical research areas. Browse published papers by subject, with three selected results, release dates and links to the current versions.",
  footer:"Only verified published works are listed. Draft DOI ≠ publication.",
  back:"← All papers",researchSummary:"RESEARCH SUMMARY",summary:"Overview",topics:"Research areas",
  versionHistory:"What changed in published versions",bibliography:"BIBLIOGRAPHY",author:"Author",
  versionDOI:"Published version DOI",conceptDOI:"All versions (Concept DOI)",
  published:"Published",details:"View paper",pdf:"PDF",tex:"TeX",source:"Repository",
  emptyHistory:"No verified public version-change notes are available yet.",
  newsEmpty:"No verified public-release notes are available yet.",error:"Unable to load the public catalogue.",
  searchPlaceholder:"Search by title, code, result or topic",otherLang:"Русский"
 },
 ru: {
  "achievementMathSetupTitle":"Математическая постановка",
  "achievementMathResultTitle":"Точный результат / доказанные границы",
  "achievementGhzExactMathNotation":"Пусть L — ненулевая вещественная n-линейная форма на (ℝᵐ)ⁿ. Её вещественная норма вычисляется на знаковых векторах {−1,1}ᵐ, а норма комплексного продолжения — на фазовых векторах 𝕋ᵐ. Супремум берётся также по m.",
  "achievementGhzExactMathDetail":"Здесь vₙ — максимальная видимость, при которой планарные полные GHZ-корреляции допускают локальную модель для любого конечного набора настроек; ζ — дзета-функция Римана.",
  "achievementGhzThreeMathNotation":"Константа κ₃=1/v₃ относится к той же GHZ-задаче. Q — набор нечётных простых чисел, входящих в неравенство Белла K7; L₃ — полученная из него точная нижняя граница.",
  "achievementGhzThreeMathDetail":"Сертификат K7 доказывает нижнюю границу; явная локальная модель даёт верхнюю. Равенство с верхней границей остаётся гипотезой.",
  "achievementMixingMathNotation":"Для σ-алгебр ℱ и 𝒢 коэффициент α измеряет сильное перемешивание. Для комплексных величин используется Cov(X,Y)=𝔼(XY)−(𝔼X)(𝔼Y), без комплексного сопряжения Y; X и Y измеримы относительно ℱ и 𝒢.",
  "achievementMixingMathDetail":"Константа точна: в P04 построены случаи равенства для комплексных величин, ограниченных по модулю единицей. K_G(2)=√2 — вещественная константа Гротендика порядка два.",
  "achievementMultilinearMathNotation":"Пусть B — n-линейная форма, вещественная на вещественных аргументах. Индикаторная норма d∞(B) определяется на наборах индикаторов событий. Дефект зависимости Δₙ — частный пример такой формы.",
  "achievementMultilinearMathDetail":"Оба коэффициента точны для форм, вещественных на вещественных аргументах. При n≥4 комплексный коэффициент выражается явной формулой κₙ; точное κ₃ остаётся неизвестным.",
  "achievementCfProfileMathNotation":"Пусть |Zⱼ|≤1 почти наверное и заданы rⱼ=|𝔼Zⱼ|. Обозначим R=∏rⱼ и S=∑arccos(rⱼ). Экстремум берётся по всем допустимым совместным законам.",
  "achievementCfProfileMathDetail":"При S≤π экстремум достигается конструкцией с общим симметричным знаком ε. Универсальная точная константа C_d — максимум профиля по r.",
  "achievementStabilityMathNotation":"Пусть P — закон на замкнутом единичном полидиске, D(P) — дефект факторизации произведения, C_d — универсальный максимум и Δ(P)=C_d−D(P). Орбита ℰ_d состоит из двухточечных экстремальных законов с общим знаком и поворотами координат.",
  "achievementStabilityMathDetail":"Для двухточечного семейства Pη с неравными весами дефицит квадратичен по η, а p-я степень транспортного расстояния линейна. Следовательно, степень 1/(2p) нельзя улучшить.",
  "achievementProblemTitle":"Какой вопрос нужно решить?",
  "achievementOriginTitle":"Откуда возникла задача?",
  "achievementImportanceTitle":"Почему это важно?",
  "achievementAnswerTitle":"Что удалось получить?",
  "achievementSourcesHeading":"Источники по этому результату",
  "achievementSourcesExplanation":"Здесь приведены работа CF Dependence, более ранние исследования и математический контекст. Эти ссылки не заменяют независимую проверку нового доказательства.",
  "sourceRoleOur":"Публикация CF",
  "sourceRoleOrigin":"История задачи",
  "sourceRolePrior":"Предыдущие результаты",
  "sourceRoleBackground":"Научный контекст",
  "sourceRoleProof":"Проверка доказательства",
  "sourceRoleRelated":"Связанная работа",
  "achievementGhzExactProblem":"Сколько шума могут выдержать измерения запутанных квантовых частиц, прежде чем их результаты можно будет объяснить локальной классической моделью?",
  "achievementGhzExactOrigin":"Вопрос вырос из неравенств Белла. Мермин в 1990 году исследовал многочастичную запутанность, а Жуковский в 1993 году — все настройки измерений. Позднее учёные уточняли границы с помощью численных методов.",
  "achievementGhzExactWhy":"Точный порог показывает, какая точность квантовых корреляций нужна, чтобы исключить рассматриваемую классическую модель. При этом не приходится выбирать ограниченное число углов измерений.",
  "achievementGhzExactAnswer":"В P04 получена точная формула для четырёх и более частиц при планарных GHZ-измерениях по полным корреляциям. Для четырёх частиц порог равен 34/105, то есть примерно 32,38%.",
  "achievementGhzThreeProblem":"Каков точный порог для трёх запутанных частиц, при котором локальная классическая модель уже не может воспроизвести все планарные GHZ-корреляции?",
  "achievementGhzThreeOrigin":"Для трёх участников задача оказалась сложнее. Работы 2023 и 2024 годов сузили область возможного ответа, но точную формулу не получили.",
  "achievementGhzThreeWhy":"Узкий доказанный интервал показывает, насколько мы близки к истинному значению. Он позволяет проверять новые неравенства Белла и новые классические модели.",
  "achievementGhzThreeAnswer":"P04 улучшает обе границы 2024 года. Нижняя получена из неравенства Белла с проверкой 272 точных рациональных неравенств, верхняя — из явной классической модели. Точная формула пока остаётся гипотезой.",
  "achievementMixingProblem":"Если две группы случайных величин лишь слабо связаны, насколько большой может оставаться ковариация ограниченных комплексных наблюдений?",
  "achievementMixingOrigin":"Для измерения такой зависимости используют коэффициент сильного перемешивания. Дворецкий (1972), Брэдли и Брыц (1985) и другие математики получили оценки ковариации, но их коэффициенты не были точными.",
  "achievementMixingWhy":"Наилучший коэффициент превращает слова «слабая зависимость» в количественную гарантию. Это важно при изучении случайных процессов и зависимых данных.",
  "achievementMixingAnswer":"P04 доказывает точный коэффициент 4√2 для ограниченных комплексных наблюдений при указанной нормировке сильного перемешивания. Для вещественных наблюдений коэффициент равен 4.",
  "achievementMultilinearProblem":"Насколько большой может быть общий эффект зависимости, если взаимодействуют три и более группы случайных величин?",
  "achievementMultilinearOrigin":"В 1985 году Брэдли и Брыц доказали общие мультлинейные оценки и указали, что их коэффициенты не наилучшие. Задача связана с анализом и геометрией квантовых корреляций.",
  "achievementMultilinearWhy":"Точные коэффициенты показывают реальные пределы взаимодействия. Слишком грубые оценки могут значительно завышать возможный эффект зависимости.",
  "achievementMultilinearAnswer":"P04 определяет точные множители для класса форм, вещественных на вещественных аргументах. Для комплексного случая при n≥4 получена явная формула. Общая задача 1985 года этим не закрыта.",
  "achievementCfProfileProblem":"Насколько сильно совместное распределение может отклониться от независимости, если модули средних его компонент уже известны?",
  "achievementCfProfileOrigin":"При независимости совместная характеристическая функция равна произведению отдельных. Эту идею давно используют в статистических критериях и мерах зависимости.",
  "achievementCfProfileWhy":"Максимально возможное отклонение задаёт естественный масштаб: становится ясно, насколько велика измеренная зависимость по сравнению с пределом.",
  "achievementCfProfileAnswer":"P01 даёт точную формулу через заданные модули средних. Например, C₃=2/√3 и C₄=9/7. В статье описаны распределения, достигающие этих границ.",
  "achievementStabilityProblem":"Если зависимость почти достигла максимума, означает ли это, что само распределение близко к экстремальному?",
  "achievementStabilityOrigin":"Обычное точное неравенство сообщает предел, но не описывает почти максимальные случаи. Теория устойчивости и расстояния Васерштейна позволяют измерить такую близость.",
  "achievementStabilityWhy":"Реальные данные редко дают идеальный максимум. Теорема показывает, что можно сказать о структуре распределения, если результат лишь немного не дотягивает до предельного.",
  "achievementStabilityAnswer":"При d≥3, конечном p≥1 и достаточно малом дефиците Δ работа P13 ограничивает расстояние Васерштейна до множества экстремалей величиной порядка Δ^(1/(2p)). Этот показатель оптимален.",
  "achievementNav":"Достижения",
  "achievementHighlightLabel":"ГЛАВНЫЕ РЕЗУЛЬТАТЫ",
  "achievementHighlightHeading":"Важные научные достижения",
  "achievementHighlightIntro":"Четыре ключевых результата. На отдельной странице каждый объяснён простым языком и снабжён 6–7 источниками.",
  "achievementHighlight1Name":"GHZ: точный порог шума для четырёх и более частиц",
  "achievementHighlight1Text":"Для четырёх частиц точный порог рассматриваемых квантовых корреляций составляет 34/105.",
  "achievementHighlight2Name":"GHZ для трёх частиц: очень узкий интервал ответа",
  "achievementHighlight2Text":"Обе границы улучшены по сравнению с прежними результатами, но предполагаемая формула с ζ(3) пока не доказана.",
  "achievementHighlight3Name":"Слабая зависимость: точная оценка ковариации",
  "achievementHighlight3Text":"Точный коэффициент 4√2 улучшает прежнюю оценку 2π для ограниченных комплексных величин.",
  "achievementHighlight4Name":"Насколько сильной может быть зависимость?",
  "achievementHighlight4Text":"P01 даёт точную формулу и наилучшие константы, включая C₃=2/√3 и C₄=9/7.",
  "achievementHighlightCTA":"Подробнее о результатах и источниках →",
  "achievementCaution":"Точные теоремы и продвижение в ещё открытых задачах отмечены раздельно. Независимая проверка доказательств и научного приоритета ещё не завершена.",
  "achievementBack":"← Обзор",
  "achievementCatalogue":"Все публикации",
  "achievementPageEyebrow":"ИЗБРАННЫЕ НАУЧНЫЕ РЕЗУЛЬТАТЫ",
  "achievementPageHeading":"Важные научные достижения",
  "achievementPageLead":"Шесть результатов простыми словами: в чём вопрос, как он возник, почему важен и что удалось доказать.",
  "achievementContextTitle":"Как читать заявления о результатах",
  "achievementContextText":"Сначала объясняем сам вопрос и его историю, затем — математический ответ и источники. Точные доказанные формулы, частичные результаты и гипотезы отделены друг от друга. Независимое ревью ещё не завершено.",
  "achievementTocGhzExact":"GHZ: точно при n≥4",
  "achievementTocGhzThree":"GHZ: три участника",
  "achievementTocMixing":"Точная ковариация",
  "achievementTocMultilinear":"Мультлинейный вопрос 1985 года",
  "achievementTocProfile":"Универсальный CF-профиль",
  "achievementTocStability":"Точная устойчивость",
  "achievementStateExact":"Точно при указанных условиях",
  "achievementStatePartial":"Границы улучшены; вопрос открыт",
  "achievementStateRestricted":"Частичный ответ; общая задача открыта",
  "achievementGhzExactTitle":"Точный порог планарной GHZ-нелокальности при n ≥ 4",
  "achievementGhzExactDescription":"В работе выведена замкнутая формула оптимального порога локальной модели для GHZ-корреляций в плоскости XY при произвольных конечных наборах углов измерения и рассмотрении полных корреляций.",
  "achievementExample":"Пример",
  "achievementGhzExactImportance":"Раньше исследователи находили строгие границы для отдельных схем измерений. Новая формула относится ко всей рассматриваемой планарной задаче о полных корреляциях, а не к одному набору углов.",
  "achievementGhzExactScope":"Речь об измерениях в плоскости XY и полных корреляциях GHZ, а не обо всех опытах Белла и произвольных измерениях. Необходимы независимая проверка доказательства и сравнение с литературой.",
  "achievementReadP04":"P04 — серия публикаций (Zenodo) ↗",
  "achievementReadDvp":"Designolle–Vértesi–Pokutta (2024) ↗",
  "achievementGhzThreeTitle":"GHZ для трёх участников: узкий интервал и гипотеза о точной формуле",
  "achievementGhzThreeDescription":"Для трёх участников точное значение пока не доказано. Статья даёт новую нижнюю границу из конечногармонического неравенства Белла и аналитическую верхнюю границу из явной локальной модели на основе меандров и функции Мёбиуса.",
  "achievementGhzThreeComparison":"В работе 2024 года порог видимости находился между 0,49129 и 0,49143. P04 улучшает обе границы. Оставшийся интервал для κ₃ составляет около 0,01775% верхней границы.",
  "achievementGhzThreeConjecture":"Предполагается, что κ₃ = 105ζ(3)/(2π³). Равенство пока не доказано.",
  "achievementGhzThreeProof":"Нижняя граница доказана аналитическим сведением и 272 точными проверками рациональных неравенств (сертификат K7). Проверка воспроизводима, но независимого внешнего ревью пока не было.",
  "achievementGhzThreeZeta":"Почему трудно получить точное равенство? Колебания, связанные с функцией Мёбиуса и нулями дзета-функции, мешают естественному построению нужного неравенства Белла. Это не равносильно гипотезе Римана.",
  "achievementMixingTitle":"Оптимальная ковариационная константа при сильном перемешивании",
  "achievementMixingDescription":"Для ограниченных комплексных случайных величин, измеримых относительно двух σ-алгебр, P04 доказывает точный коэффициент ковариационного неравенства через классический коэффициент сильного перемешивания α.",
  "achievementMixingHistory":"Прежняя оценка Дворецкого использовала коэффициент 2π (около 6,28). В P04 получен меньший точный коэффициент 4√2 (около 5,66). Для вещественных величин он равен 4.",
  "achievementMixingScope":"Сравнение верно при одинаковом определении сильного перемешивания и нормировке. Для заявления о мировом приоритете ещё нужна отдельная проверка литературы.",
  "achievementReadBradley":"Bradley–Bryc (1985) ↗",
  "achievementMultilinearTitle":"Уточнение мультлинейных оценок и вопрос 1985 года",
  "achievementMultilinearDescription":"В 1985 году Bradley и Bryc указали, что коэффициенты их общего мультлинейного неравенства неоптимальны. В P04 получены точные вещественные и комплексные множители 2ⁿ и 2ⁿκₙ для естественного класса форм, принимающих вещественные значения на вещественных аргументах.",
  "achievementMultilinearScope":"Вопрос 1985 года охватывает все комплексные мультлинейные формы. P04 доказывает точный ответ для более узкого естественного класса. Общая задача и точный комплексный коэффициент при n=3 остаются открытыми.",
  "achievementProfileTitle":"Универсальный профиль зависимости через характеристические функции",
  "achievementProfileDescription":"Экстремальная задача по совместным законам ограниченных комплексных величин сведена к явной формуле через заданные модули их средних. Это объединяет несколько задач факторизации характеристических функций.",
  "achievementProfileImportance":"Например, C₂=1, C₃=2/√3 и C₄=9/7. Построены распределения, достигающие границ; при росте числа компонент C_d стремится к 2. Мы не объявляем это решением ранее известной старой проблемы без отдельной проверки.",
  "achievementReadP01":"P01 — серия публикаций (Zenodo) ↗",
  "achievementStabilityTitle":"Точная количественная устойчивость вблизи экстремальной зависимости",
  "achievementStabilityDescription":"P13 усиливает точное неравенство теоремой об устойчивости: если дефект зависимости близок к максимуму, совместное распределение близко ко всему семейству случаев равенства.",
  "achievementStabilityScope":"При d≥3, конечном p≥1 и достаточно малом дефиците Δ показатель 1/(2p) оптимален. Для другой, более структурированной меры отклонения получена точная оценка порядка √Δ.",
  "achievementStabilityPriority":"Это точная математическая теорема. Но независимого подтверждения, что она решает ранее сформулированную старую открытую проблему, пока нет.",
  "achievementReadP13":"P13 — серия публикаций (Zenodo) ↗",
  "achievementEditorialTitle":"Доказательства, новизна и приоритет",
  "achievementEditorialText":"Под каждым достижением приведено 6–7 источников: наша публикация, предшествующие результаты и научный контекст. Ссылки помогают проследить историю вопроса, но не заменяют независимой проверки доказательств.",
  "achievementEditorialSecond":"Формула для GHZ с тремя участниками остаётся гипотезой. Общая комплексная мультлинейная задача 1985 года тоже не решена полностью. Мы этого не скрываем.",
  "achievementAllPapers":"Посмотреть все опубликованные статьи →",
  papers:"Работы",updates:"Что изменилось",about:"О проекте",eyebrow:"ЭКСТРЕМАЛЬНАЯ ВЕРОЯТНОСТЬ · АНАЛИЗ · АЛГЕБРА",
  hero:"Исследовательская программа по зависимости через характеристические функции, точным неравенствам и математической структуре экстремалей.",
  programmeLabel:"НАУЧНАЯ ПРОГРАММА",programmeHeading:"Что исследует CF Dependence",
  programmeLead:"Проект возник из исследования зависимости через характеристические функции и теперь изучает математические структуры взаимодействия, их наблюдения, ограничения и экстремальные свойства.",
  programmeObjectHeading:"Объект исследования",
  programmeObject:"Пусть P — совместное распределение с маргиналями P₁, …, P_d. Основной объект — знаковая мера взаимодействия: разность совместного распределения и произведения его маргиналей.",
  programmeObjectNote:"Дефект факторизации характеристических функций — исходный способ наблюдения, но не граница проекта. Другие нормы, гармонические представления, транспорт и меры взаимодействия открывают новые экстремальные задачи.",
  programmeGoalHeading:"Цель исследования",
  programmeGoal:"Открывать новые математические законы, доказывать их аналитически там, где это возможно, и выявлять общие механизмы, объясняющие целые классы результатов, а не отдельные примеры.",
  programmeMethodHeading:"Как ведётся исследование",
  programmeMethod:"Исследуем примеры, вычислительные эксперименты и контрпримеры; выделяем инварианты и существенные координаты; формулируем явный закон, строго доказываем его и проверяем перенос механизма на другие задачи. В центре внимания — точные границы, экстремизаторы, случаи равенства и устойчивость.",
  programmeBridge:"Расположенные выше публикации по областям показывают развитие программы: точные неравенства, заданные маргинали и транспорт, алгебру, гармонические методы восстановления и статистику.",
  areasNav:"По областям",areasLabel:"КАРТА ИССЛЕДОВАНИЙ",areasHeading:"Публикации по научным областям",
  keyResultsHeading:"Основные результаты",resultsLabel:"Что доказано или установлено",
  resultsFromVersion:"Результаты изложены по опубликованной версии",areasIntro:"Аннотированный научный каталог: для каждой статьи приведены краткий обзор и три выбранных результата из проверенного опубликованного текста.",
  areasUnavailable:"Не удалось отобразить каталог публикаций. Перезагрузите страницу и попробуйте ещё раз.",
  firstPublished:"Первая публикация",lastChanged:"Последнее обновление",
  latestVersionNumber:"Последняя версия",unknownVersion:"Номер версии не подтверждён",zenodoOrdinal:"Выпуск Zenodo",
  publicationDateNote:"Даты относятся к опубликованным версиям Zenodo, а не к изменениям сайта.",
  verifiedAsOf:"Каталог сверён по состоянию на",zenodoUpdated:"Публичные данные Zenodo обновлены",missingDate:"Дата не подтверждена",releaseDate:"Дата публикации",
  versionIdentifier:"DOI проверенной версии",openLatest:"Открыть актуальную версию",
  latestPublished:"Актуальная публикация (Concept DOI)",lastVerifiedDate:"Дата последней проверенной публикации",
  verifiedVersionDOI:"DOI проверенной версии (для цитирования)",
  doiExplanation:"Даты относятся к первой и последней опубликованным версиям Zenodo, а не к правкам сайта. Concept DOI ведёт к актуальной версии, DOI версии фиксирует конкретный выпуск.",
  olderPdf:"Архивный PDF",olderTex:"Архивный TeX",zenodoPDF:"PDF в Zenodo",
  publishedLabel:"ОПУБЛИКОВАННЫЕ РАБОТЫ",papersHeading:"Научные статьи",publishedCount:"опубликованные работы",
  searchLabel:"Поиск работ",noMatches:"Ничего не найдено.",
  newsLabel:"ОБНОВЛЕНИЯ ПРОЕКТА",updatesHeading:"Что изменилось",
  updatesInfo:"Подтверждённые изменения сайта и выпуски научных работ в обратном хронологическом порядке.",
  siteUpdateKind:"Обновление сайта",publicationUpdateKind:"Публикация",
  olderUpdatesLabel:"Ранее в проекте",
  staticUpdateP19Title:"P19: синтез зависимости при заданных маргиналях",
  staticUpdateP19Text:"Новая работа: совместные распределения с ограничениями на моменты, спектральные нули и преобразования Фурье.",
  staticUpdateP20Title:"P20: статистическое оценивание экстремальной зависимости",
  staticUpdateP20Text:"Новая работа: растущие частотные профили, случайные наборы частот и калибровка Уолша.",
  staticUpdateCollectionTitle:"CF V6: добавлено пятнадцать научных работ",
  staticUpdateCollectionText:"Публичный каталог расширился с трёх до восемнадцати исследований.",
  staticUpdateInitialTitle:"Первый публичный набор рукописей",
  staticUpdateInitialText:"В открытом репозитории опубликованы первые три рукописи P01–P03.",
  staticUpdateMathTitle:"Добавлены строгие математические постановки",
  staticUpdateMathText:"Во всех шести достижениях появились определения, условия теорем и точные формулы; на главной размещены четыре короткие формулы.",
  staticUpdateSourcesTitle:"Каждый результат получил своё объяснение и источники",
  staticUpdateSourcesText:"В каждом из шести разделов объяснены задача, её происхождение, значимость и результат, а также приведены 6–7 отдельных источников.",
  authorNav:"Об авторе",authorLabel:"ИССЛЕДОВАТЕЛЬ",authorHeading:"Об авторе",
  authorRole:"Независимый исследователь",
  aiDisclosureLabel:"ПРОЗРАЧНОСТЬ ИССЛЕДОВАНИЙ",aiDisclosureHeading:"Участие искусственного интеллекта",
  aiDisclosureText:"Исследования CF Dependence выполнялись автором совместно с системами искусственного интеллекта (ИИ). ИИ участвовал в математическом поиске, разработке и критическом анализе идей и доказательств, а также в подготовке рукописей. Системы ИИ не указаны в качестве соавторов. За опубликованные утверждения, доказательства и выводы отвечает автор.",
  aboutLabel:"НАПРАВЛЕНИЯ И ПУБЛИКАЦИИ",aboutHeading:"О проекте CF Dependence",
  aboutText:"Пять взаимосвязанных направлений математики. Ниже — опубликованные статьи по областям с тремя выбранными результатами, датами выпусков и ссылками на актуальные версии.",
  footer:"Только подтверждённые опубликованные работы. Зарезервированный DOI ≠ публикация.",
  back:"← Все работы",researchSummary:"СОДЕРЖАНИЕ",summary:"Обзор",topics:"Области исследований",
  versionHistory:"Изменения в опубликованных версиях",bibliography:"БИБЛИОГРАФИЯ",author:"Автор",
  versionDOI:"DOI опубликованной версии",conceptDOI:"Все версии (Concept DOI)",
  published:"Опубликовано",details:"Открыть статью",pdf:"PDF",tex:"TeX",source:"Репозиторий",
  emptyHistory:"Пока нет подтверждённых заметок об изменениях опубликованных версий.",
  newsEmpty:"Пока нет подтверждённых публичных обновлений.",error:"Не удалось загрузить каталог.",
  searchPlaceholder:"Поиск по названию, коду, результатам или теме",otherLang:"English"
 }
};
const RESEARCH_AREAS = [
  {id:"extremal",name:{en:"Extremal dependence and sharp inequalities",ru:"Экстремальная зависимость и точные неравенства"},
   description:{en:"Universal bounds, extremal profiles, stability and higher-order interaction measures.",
    ru:"Универсальные оценки, экстремальные профили, устойчивость и многомерные меры взаимодействия."}},
  {id:"transport",name:{en:"Prescribed marginals and optimal transport",ru:"Заданные маргинали и оптимальный транспорт"},
   description:{en:"Couplings, mixability, transport geometry and the construction of prescribed dependence.",
    ru:"Совместные распределения, смешиваемость, геометрия транспорта и синтез зависимости."}},
  {id:"algebra",name:{en:"Polynomial algebra, Galois theory and moments",ru:"Алгебра полиномов, теория Галуа и моменты"},
   description:{en:"Chebyshev–Lucas polynomials, critical points, resultants and arithmetic moment reconstruction.",
    ru:"Полиномы Чебышёва—Люкаса, критические точки, результанты и арифметика моментов."}},
  {id:"harmonic",name:{en:"Harmonic analysis and inverse problems",ru:"Гармонический анализ и обратные задачи"},
   description:{en:"Recovering hidden structures from Fourier, Walsh and finite-group observations.",
    ru:"Восстановление скрытых структур по наблюдениям Фурье, Уолша и конечных групп."}},
  {id:"statistics",name:{en:"Statistical tests and estimation",ru:"Статистические критерии и оценивание"},
   description:{en:"Independence tests, robust methods and estimating dependence functionals.",
    ru:"Критерии независимости, робастные методы и оценивание функционалов зависимости."}}
];
const DOI = /^10\.5281\/zenodo\.\d+$/;
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;
function versionName(p) {
  if (typeof p.version_label === "string" && /^[A-Za-z0-9][A-Za-z0-9._+\- ]{0,47}$/.test(p.version_label))
    return p.version_label;
  if (Number.isInteger(p.version_index) && p.version_index > 0)
    return COPY[language].zenodoOrdinal+" №"+p.version_index;
  return COPY[language].unknownVersion;
}
function metadataValueLine(label, value, date=false) {
  const line=node("div","area-metadata-line");
  line.appendChild(node("span","area-meta-label",label));
  if(date && typeof value==="string" && ISO_DATE.test(value)) {
    const stamp=node("time","area-meta-value",value);
    stamp.dateTime=value;
    line.appendChild(stamp);
  } else {
    line.appendChild(node("span","area-meta-value",value || COPY[language].missingDate));
  }
  return line;
}
function lastVersionDate(p) { return p.last_version_on || p.published_on || ""; }
let language = new URLSearchParams(location.search).get("lang") === "ru" ? "ru" : "en";
let papers = [];
let news = [];
let newsLoaded = false;
let catalogueDate = "";
let zenodoCheckedDate = "";
let zenodoResolvedCount = 0;
const $ = (id) => document.getElementById(id);
function node(tag, className, text) {
  const el = document.createElement(tag);
  if (className) el.className = className;
  if (text !== undefined) el.textContent = text;
  return el;
}
function children(parent, ...nodes) { for(const n of nodes) parent.appendChild(n); return parent; }
function applyLanguage() {
  document.documentElement.lang = language;
  for (const el of document.querySelectorAll("[data-i18n]")) {
    const key=el.dataset.i18n;
    if(COPY[language][key])el.textContent=COPY[language][key];
  }
  const search=$("search"); if(search) search.placeholder=COPY[language].searchPlaceholder;
  for (const link of document.querySelectorAll("[data-achievements-link]"))
    link.href="achievements.html?lang="+language+(link.hash||"");
  for (const link of document.querySelectorAll("[data-achievement-home-link]"))
    link.href="index.html?lang="+language+"#achievements";
  for (const link of document.querySelectorAll("[data-catalogue-home-link]"))
    link.href="index.html?lang="+language+"#areas";
  for (const link of document.querySelectorAll("[data-home-link]"))
    link.href="index.html?lang="+language;
  for (const btn of document.querySelectorAll("[data-lang-switch]")) btn.textContent=COPY[language].otherLang;
  const url=new URL(location.href); url.searchParams.set("lang",language);
  history.replaceState(null,"",url);
}
function doiLink(doi, label=doi) {
  const el=node("a",null,label+" ↗");
  if (!DOI.test(doi)) { el.removeAttribute("href"); return el; }
  el.href="https://doi.org/"+doi;
  el.target="_blank";el.rel="noopener noreferrer";return el;
}
function publicRepoLink(p, file) {
  if (!/^papers\/[a-z0-9-]+$/.test(p.source_path)) return "#";
  return "https://github.com/alexmartinevski/CF-Dependence-Public/blob/main/"+p.source_path+(file?"/"+file:"");
}
function verifiedPapers(input) {
  if(!Array.isArray(input))throw new Error("Invalid catalogue");
  return input.filter(p=>p.status==="published" && DOI.test(p.version_doi) && DOI.test(p.concept_doi));
}
function renderAreas(visiblePapers=papers) {
  const container=$("area-groups");
  if(!container)return;
  const note=$("area-snapshot");
  note.textContent=COPY[language].verifiedAsOf+": "+(catalogueDate||"—")+"."+(zenodoResolvedCount>0?" "+COPY[language].zenodoUpdated+": "+zenodoCheckedDate+" ("+zenodoResolvedCount+"/"+papers.length+").":"")+" "+COPY[language].publicationDateNote;
  container.replaceChildren();
  for(const area of RESEARCH_AREAS) {
    const members=visiblePapers.filter(p=>p.area===area.id);
    if(!members.length)continue;
    const group=node("section","area-group");
    const heading=node("div","area-group-heading");
    const title=node("h3",null,area.name[language]);
    const count=node("span","area-group-count",String(members.length));
    const description=node("p","area-group-description",area.description[language]);
    heading.append(title,count,description);
    const rows=node("div","area-rows");
    for(const p of members) {
      const item=node("article","area-row");
      const main=node("div","area-row-main");
      const headline=node("div","area-headline");
      const link=node("a","area-paper-link",p.title);
      link.href="paper.html?code="+encodeURIComponent(p.code)+"&lang="+language;
      headline.append(node("span","code",p.code),link);
      main.append(headline,node("p","area-paper-summary",p.summary[language]||p.summary.en));
      const highlights=node("ul","area-highlights");
      for(const fact of p.highlights||[]) {
        const li=node("li",null,fact[language]||fact.en);
        highlights.appendChild(li);
      }
      const resultHeading=node("p","area-results-label",COPY[language].resultsLabel);
      main.append(resultHeading,highlights);
      const meta=node("div","area-row-meta");
      const firstBlock=metadataValueLine(COPY[language].firstPublished,p.first_published_on,true);
      const updateBlock=metadataValueLine(COPY[language].lastChanged,lastVersionDate(p),true);
      const versionBlock=metadataValueLine(COPY[language].latestVersionNumber,versionName(p));
      const citationBlock=node("div","area-metadata-line");
      citationBlock.append(node("span","area-meta-label",COPY[language].versionIdentifier),doiLink(p.version_doi,p.version_doi));
      const current=doiLink(p.concept_doi,COPY[language].openLatest);
      current.className="area-latest-link";
      meta.append(firstBlock,updateBlock,versionBlock,citationBlock,current);
      // Public scientific claims remain anchored to the version whose text was checked.
      if(DOI.test(p.highlights_source_doi) && p.highlights_source_doi!==p.version_doi) {
        const provenance=node("div","area-metadata-line");
        provenance.append(node("span","area-meta-label",COPY[language].resultsFromVersion),doiLink(p.highlights_source_doi));
        meta.appendChild(provenance);
      }
      item.append(main,meta);
      rows.appendChild(item);
    }
    group.append(heading,rows);
    container.appendChild(group);
  }
  // The no-match state is rendered separately by renderIndex.
}
function renderIndex() {
  applyLanguage();
  const query=($("search")?.value||"").trim().toLocaleLowerCase();
  const matching=papers.filter(p=>{
    const subject=RESEARCH_AREAS.find(a=>a.id===p.area);
    const searchable=[p.code,p.title,p.summary.en,p.summary.ru,...(p.topics||[]),
      ...(p.highlights||[]).flatMap(x=>[x.en,x.ru]),
      subject?.name.en,subject?.name.ru].filter(Boolean).join(" ").toLocaleLowerCase();
    return searchable.includes(query);
  });
  try { renderAreas(matching); }
  catch (error) {
    const areaContainer=$("area-groups");
    if(areaContainer)areaContainer.replaceChildren(node("p","muted",COPY[language].areasUnavailable));
    console.error("Subject directory rendering failed",error);
  }
  $("paper-count").textContent=String(matching.length);
  $("no-matches").classList.toggle("hidden",matching.length!==0);
  if(newsLoaded)renderUpdates($("news-items"),true);
}
function updateSource(source) {
  if(typeof source!=="string") return null;
  if(source.startsWith("https://doi.org/") && DOI.test(source.slice("https://doi.org/".length)))
    return {url:source,label:source.slice("https://doi.org/".length)};
  const pr=source.match(/^https:\/\/github\.com\/alexmartinevski\/CF-Dependence-Public\/pull\/([1-9][0-9]*)$/);
  if(pr)return {url:source,label:"GitHub PR #"+pr[1]};
  if(source==="RELEASE_NOTES.md")
    return {url:"https://github.com/alexmartinevski/CF-Dependence-Public/blob/main/RELEASE_NOTES.md",label:"RELEASE_NOTES.md"};
  return null;
}
function story(date, title, summary, source, kind="publication_release") {
  const article=node("article","news-item");
  const meta=node("div","news-meta");
  const time=node("time",null,date); time.dateTime=date;
  const type=node("span","news-type",kind==="site_update"?COPY[language].siteUpdateKind:COPY[language].publicationUpdateKind);
  meta.append(time,type);
  const h=node("h3",null,title);
  const p=node("p",null,summary);
  article.append(meta,h,p);
  const citation=updateSource(source);
  if(citation) {
    const a=node("a","news-source",citation.label+" ↗");
    a.href=citation.url; a.target="_blank"; a.rel="noopener noreferrer";
    article.appendChild(a);
  }
  return article;
}
function allUpdates() {
  const items=[...news.map(x=>({date:x.date,title:x.title[language],summary:x.summary[language],source:x.source||null,kind:x.kind||"publication_release"}))];
  for (const p of papers) for (const c of p.changes||[]) {
    if (!DOI.test(c.doi) || !c.date) continue;
    items.push({date:c.date,title:p.code+" · "+p.title,summary:c.summary[language]||c.summary.en,source:"https://doi.org/"+c.doi});
  }
  return items.sort((a,b)=>b.date.localeCompare(a.date));
}
// Keep the home-page news grid exactly two rows × two columns on desktop.
// Earlier events remain accessible in the native expandable archive.
const HOME_NEWS_LIMIT=4;
function renderUpdates(parent, includeSiteNews) {
  const events=includeSiteNews?allUpdates():[];
  const history=$("older-news-items");
  const archive=$("news-archive");
  parent.replaceChildren();
  if(history)history.replaceChildren();
  if(!events.length) {
    parent.appendChild(node("p","muted",COPY[language].newsEmpty));
    if(archive)archive.hidden=true;
    return;
  }
  for(const e of events.slice(0,HOME_NEWS_LIMIT))
    parent.appendChild(story(e.date,e.title,e.summary,e.source,e.kind));
  const older=events.slice(HOME_NEWS_LIMIT);
  if(history)for(const e of older)
    history.appendChild(story(e.date,e.title,e.summary,e.source,e.kind));
  if(archive)archive.hidden=older.length===0;
}
function renderDetail() {
  applyLanguage();
  const code=new URLSearchParams(location.search).get("code");
  const p=papers.find(x=>x.code===code);
  if(!p){$("paper-title").textContent=COPY[language].error;return;}
  document.title=p.title+" — CF Dependence";
  $("paper-code").textContent=p.code+" · "+COPY[language].published;
  $("paper-title").textContent=p.title;
  $("paper-summary").textContent=p.summary[language]||p.summary.en;
  $("paper-description").textContent=p.summary[language]||p.summary.en;
  const results=$("paper-results");
  results.replaceChildren(...(p.highlights||[]).map(x=>node("li",null,x[language]||x.en)));
  const source=$("paper-results-source");
  source.replaceChildren();
  if(DOI.test(p.highlights_source_doi)){
    source.append(node("span",null,COPY[language].resultsFromVersion+": "),doiLink(p.highlights_source_doi));
  }
  const tags=$("paper-topics");tags.replaceChildren(...(p.topics||[]).map(x=>node("span","tag",x)));
  $("paper-latest").replaceChildren(doiLink(p.concept_doi,COPY[language].openLatest));
  $("paper-version").replaceChildren(doiLink(p.version_doi,p.version_doi));
  $("paper-first-published").textContent=p.first_published_on||COPY[language].missingDate;
  $("paper-last-updated").textContent=lastVersionDate(p)||COPY[language].missingDate;
  $("paper-version-number").textContent=versionName(p);
  const links=$("paper-downloads");links.replaceChildren();
  const downloads=[];
  // The current PDF must be retrieved from the Zenodo concept record, never
  // mistaken for an older GitHub snapshot or an exact-version record URL.
  downloads.push([COPY[language].zenodoPDF,"https://doi.org/"+p.concept_doi]);
  if (p.source_path) {
    downloads.push([COPY[language].olderPdf,publicRepoLink(p,"paper.pdf")]);
    downloads.push([COPY[language].olderTex,publicRepoLink(p,"paper.tex")]);
    downloads.push([COPY[language].source,publicRepoLink(p,null)]);
  }
  for(const [name,url] of downloads){const a=node("a",null,name+" ↗");a.href=url;a.target="_blank";a.rel="noopener noreferrer";links.appendChild(a);}
  const history=$("paper-history");history.replaceChildren();
  const changes=(p.changes||[]).filter(x=>DOI.test(x.doi)).sort((a,b)=>b.date.localeCompare(a.date));
  if(!changes.length)history.appendChild(node("p","muted",COPY[language].emptyHistory));
  else for(const c of changes)history.appendChild(story(c.date,c.version||p.title,c.summary[language]||c.summary.en,"https://doi.org/"+c.doi));
}
async function init() {
  const buttons=document.querySelectorAll("[data-lang-switch]");
  for(const b of buttons)b.addEventListener("click",()=>{language=language==="en"?"ru":"en";if(document.body.dataset.page==="index")renderIndex();else if(document.body.dataset.page==="paper")renderDetail();else applyLanguage();});
  applyLanguage();
  if(document.body.dataset.page==="achievements")return;
  try{
    // Publications are mandatory, but a temporary news.json failure must never
    // hide either the catalogue or the two static, dated update cards.
    const [a,b]=await Promise.all([
      fetch("data/papers.json",{cache:"no-store"}),
      fetch("data/news.json",{cache:"no-store"}).catch(()=>null)
    ]);
    if(!a.ok)throw new Error("Unable to load published catalogue");
    const pdata=await a.json();
    let ndata=null;
    if(b && b.ok) {
      try {ndata=await b.json();} catch(error) {
        console.warn("Updates feed unavailable; retaining static website updates",error);
      }
    }
    papers=verifiedPapers(pdata.papers).sort((x,y)=>Number(x.code.slice(1))-Number(y.code.slice(1)));
    catalogueDate=typeof pdata.last_curated_on==="string"?pdata.last_curated_on:"";
    // Optional same-origin metadata generated by read-only Zenodo API at deploy time.
    // When unavailable, the explicitly dated curated catalogue remains the fallback.
    try {
      const r=await fetch("data/zenodo_latest.json",{cache:"no-store"});
      if(r.ok) {
        const latest=await r.json();
        if((latest.schema===1 || latest.schema===2) && latest.records && typeof latest.records==="object") {
          let resolved=0;
          for(const p of papers) {
            const item=latest.records[p.code];
            if(!item || item.concept_doi!==p.concept_doi || !DOI.test(item.version_doi))continue;
            const changed=item.version_doi!==p.version_doi;
            p.version_doi=item.version_doi;
            const releaseDate=item.last_version_on||item.published_on;
            if(typeof releaseDate==="string" && ISO_DATE.test(releaseDate)) {
              p.last_version_on=releaseDate;
              p.published_on=releaseDate;
            } else if(changed) {
              delete p.last_version_on;
              delete p.published_on;
            }
            if(typeof item.first_published_on==="string" && ISO_DATE.test(item.first_published_on))
              p.first_published_on=item.first_published_on;
            if(typeof item.version_label==="string" && /^[A-Za-z0-9][A-Za-z0-9._+\- ]{0,47}$/.test(item.version_label))
              p.version_label=item.version_label;
            else if(changed) delete p.version_label;
            if(Number.isInteger(item.version_index) && item.version_index>0)
              p.version_index=item.version_index;
            else if(changed) delete p.version_index;
            resolved++;
          }
          zenodoResolvedCount=resolved;
          if(typeof latest.checked_on==="string" && /^\d{4}-\d{2}-\d{2}$/.test(latest.checked_on))
            zenodoCheckedDate=latest.checked_on;
        }
      }
    }catch(error) {
      // No public metadata must never break the site's published catalogue.
    }
    newsLoaded=Array.isArray(ndata?.entries);
    news=newsLoaded?ndata.entries:[];
    if(document.body.dataset.page==="index") {
      $("search").addEventListener("input",renderIndex);
      renderIndex();
    } else renderDetail();
  }catch(error) {
    const target=$("area-groups")||$("paper-title");
    if(target)target.textContent=COPY[language].error;
  }
}
document.addEventListener("DOMContentLoaded",init);
