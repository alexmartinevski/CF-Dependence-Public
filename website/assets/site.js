"use strict";
const COPY = {
 en: {
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
  "achievementHighlightIntro":"A concise overview of the strongest published results, with a detailed mathematical account, historical sources and explicit limits of current claims.",
  "achievementHighlight1Name":"Exact planar GHZ threshold for n≥4",
  "achievementHighlight1Text":"A general formula for the sharp XY full-correlation GHZ threshold; for four parties the critical visibility is 34/105.",
  "achievementHighlight2Name":"Three-party GHZ: narrower rigorous bounds",
  "achievementHighlight2Text":"Both bounds improve the 2024 interval, while the proposed exact value 105ζ(3)/(2π³) remains a conjecture.",
  "achievementHighlight3Name":"Sharp complex covariance coefficient",
  "achievementHighlight3Text":"The coefficient 4√2 in a strong-mixing covariance inequality improves the classical 2π estimate.",
  "achievementHighlight4Name":"Exact universal dependence profile",
  "achievementHighlight4Text":"An explicit extremal profile for characteristic-function factorization defects and sharp constants C₃=2/√3, C₄=9/7.",
  "achievementHighlightCTA":"Read the detailed achievements →",
  "achievementCaution":"Exact mathematical results and improvements in still-open problems are identified separately. External proof and priority reviews have not yet been completed.",
  "achievementBack":"← Overview",
  "achievementCatalogue":"All papers",
  "achievementPageEyebrow":"SELECTED SCIENTIFIC RESULTS",
  "achievementPageHeading":"Research achievements",
  "achievementPageLead":"Exact extremal theorems, progress on historically studied bounds, and a tightly bounded open problem in planar quantum correlations.",
  "achievementContextTitle":"What these claims mean",
  "achievementContextText":"The results below are stated in released CF Dependence manuscripts. An exact formula inside its stated mathematical class is distinguished from a partial improvement or an unsolved conjecture. Independent proof and historical-priority reviews remain pending; we do not claim that every broader classical problem has been solved.",
  "achievementTocGhzExact":"GHZ: exact n≥4",
  "achievementTocGhzThree":"GHZ: three parties",
  "achievementTocMixing":"Sharp covariance",
  "achievementTocMultilinear":"1985 multilinear question",
  "achievementTocProfile":"Universal CF profile",
  "achievementTocStability":"Sharp stability",
  "achievementStateExact":"Exact result in the stated class",
  "achievementStatePartial":"Strict bounds; exact value remains open",
  "achievementStateRestricted":"Partial response in a restricted class",
  "achievementGhzExactTitle":"Exact planar GHZ threshold for n ≥ 4",
  "achievementGhzExactDescription":"The paper derives a closed formula for the optimal local-hidden-variable threshold in the planar XY, full-correlation GHZ scenario, allowing arbitrary finite sets of measurement angles.",
  "achievementExample":"Example",
  "achievementGhzExactImportance":"Unlike finite-setting numerical estimates, this is an expression for the full continuum-of-settings optimization in the specified full-correlator model. The earlier 2024 work by Designolle, Vértesi and Pokutta supplied rigorous bounds rather than this general closed formula.",
  "achievementGhzExactScope":"Scope: planar XY measurements and full correlations. This is not a claim about every Bell scenario or arbitrary measurements. Independent verification of the proof and of historical priority has not yet been completed.",
  "achievementReadP04":"P04 — published series (Zenodo) ↗",
  "achievementReadDvp":"Designolle–Vértesi–Pokutta (2024) ↗",
  "achievementGhzThreeTitle":"Three-party GHZ: a narrow interval and an exact-value conjecture",
  "achievementGhzThreeDescription":"For three parties the sharp value is not yet proved. The published paper provides a new finite-harmonic Bell lower bound and an analytical upper bound from an explicit square-wave/Möbius local model.",
  "achievementGhzThreeComparison":"These two visibility bounds improve both ends of the interval 0.49129–0.49143 reported by Designolle, Vértesi and Pokutta in 2024. The remaining κ₃ interval is only about 0.01775% of its upper bound.",
  "achievementGhzThreeConjecture":"Conjecture: the upper bound is exact, κ₃ = 105ζ(3)/(2π³). This equality has not been proved.",
  "achievementGhzThreeProof":"The lower bound uses an analytic reduction followed by 272 reproducible rational inequalities in the K7 certificate. This is computer-assisted proof, not an independent external proof-review.",
  "achievementGhzThreeZeta":"The remaining dual Bell-functional construction encounters arithmetic oscillations linked to the Möbius function and zeros of the Riemann zeta function. This does not make the conjecture equivalent to the Riemann hypothesis.",
  "achievementMixingTitle":"Optimal covariance constant under strong mixing",
  "achievementMixingDescription":"For bounded complex random variables measurable with respect to two σ-fields, P04 establishes the sharp coefficient in the covariance inequality with the classical strong-mixing coefficient α.",
  "achievementMixingHistory":"The literature contains Dvoretzky's historical bound 2π, discussed in Bradley–Bryc (1985). The constant 4√2 is smaller and is claimed sharp in P04, with an equality construction; for real scalars the constant is 4.",
  "achievementMixingScope":"This comparison uses the strong-mixing coefficient and the same bounded-observable normalization. A complete search for equivalent earlier sharp results and an independent proof review are still outstanding, so no first-ever priority is claimed.",
  "achievementReadBradley":"Bradley–Bryc (1985) ↗",
  "achievementMultilinearTitle":"Sharper multilinear estimates and the question from 1985",
  "achievementMultilinearDescription":"Bradley and Bryc observed in 1985 that their general multilinear coefficients were not optimal. P04 derives sharp real and complex factors 2ⁿ and 2ⁿκₙ for a natural class of multilinear forms real-valued on real arguments.",
  "achievementMultilinearScope":"Important distinction: the 1985 result allowed general complex multilinear forms, whereas the sharp factors in P04 concern a real-on-real subclass. Consequently the old problem is not solved in its full generality. The n=3 complex sharp factor also remains open.",
  "achievementProfileTitle":"Universal characteristic-function dependence profile",
  "achievementProfileDescription":"An extremum over joint laws of bounded complex random variables is reduced to a formula in the prescribed moduli of their means. This unifies several characteristic-function factorization problems.",
  "achievementProfileImportance":"The universal constant has explicit values C₂=1, C₃=2/√3, C₄=9/7. Extremal constructions use a common fair sign in the corresponding regime; C_d increases to 2. This is a proven exact profile, not a claim that an independently documented century-old open question was solved.",
  "achievementReadP01":"P01 — published series (Zenodo) ↗",
  "achievementStabilityTitle":"Sharp quantitative stability near extremal dependence",
  "achievementStabilityDescription":"P13 strengthens the sharp inequality into a stability theorem: if the dependence defect is close to its maximum, the joint distribution must be close to the entire family of equality cases.",
  "achievementStabilityScope":"For d≥3, any finite p≥1 and sufficiently small deficit Δ, the displayed Wasserstein exponent is optimal, even after optimizing coordinate phases. A structured discrepancy separating location and mass errors admits an optimal square-root rate.",
  "achievementStabilityPriority":"The theorem is highlighted for its exact exponent and extremal geometry, not as an independently verified solution of an older externally posed question.",
  "achievementReadP13":"P13 — published series (Zenodo) ↗",
  "achievementEditorialTitle":"Proof, novelty and priority",
  "achievementEditorialText":"A result may be mathematically precise yet still require an independent check of its proof or literature priority. The links above are to public papers or historical sources. The displayed categories refer to the claims made in the publications and their proved or unresolved scope; they are not independent peer-review certifications.",
  "achievementEditorialSecond":"The three-party GHZ formula remains a conjecture. The broad 1985 complex multilinear problem is not claimed solved. We do not present any result as the first-ever solution of a long-standing problem without both a proof review and a documented priority comparison.",
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
  programmeBridge:"The publications below develop connected parts of this programme: sharp inequalities, prescribed marginals and transport, algebra, harmonic reconstruction and statistics.",
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
  newsLabel:"RELEASE HISTORY",updatesHeading:"What's new",
  updatesInfo:"Verified public-release notes only. DOI reservations and private reviews do not appear as publications.",
  authorNav:"Author",authorLabel:"RESEARCHER",authorHeading:"About the author",
  authorRole:"Independent Researcher",
  aiDisclosureLabel:"RESEARCH TRANSPARENCY",aiDisclosureHeading:"AI collaboration disclosure",
  aiDisclosureText:"CF Dependence research was conducted by the author in collaboration with artificial intelligence (AI) systems. AI assisted with mathematical exploration, developing and critically examining ideas and proofs, and preparing manuscripts. AI systems are not listed as co-authors. The author is responsible for the published mathematical statements, proofs, and conclusions.",
  aboutLabel:"THE PROJECT",aboutHeading:"About CF Dependence",
  aboutText:"An evolving mathematical research programme bringing together extremal probability, fixed-marginal dependence, and algebraic methods. This catalogue links to published versions and their public research materials.",
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
  "achievementHighlightIntro":"Краткий обзор наиболее значимых опубликованных результатов. На отдельной странице — формулы, историческое сравнение, первоисточники и границы научных утверждений.",
  "achievementHighlight1Name":"Точный планарный порог GHZ при n≥4",
  "achievementHighlight1Text":"Общая формула порога планарной GHZ-нелокальности по полным корреляциям: для четырёх участников критическая видимость 34/105.",
  "achievementHighlight2Name":"GHZ для трёх участников: новые строгие границы",
  "achievementHighlight2Text":"Обе границы улучшены по сравнению с опубликованным интервалом 2024 года. Предполагаемое точное значение 105ζ(3)/(2π³) пока не доказано.",
  "achievementHighlight3Name":"Точная комплексная ковариационная константа",
  "achievementHighlight3Text":"Константа 4√2 в оценке ковариации через сильное перемешивание улучшает классическую оценку 2π.",
  "achievementHighlight4Name":"Универсальный точный профиль зависимости",
  "achievementHighlight4Text":"Явная формула экстремального дефекта факторизации характеристических функций и точные константы C₃=2/√3, C₄=9/7.",
  "achievementHighlightCTA":"Подробнее о достижениях →",
  "achievementCaution":"Точные теоремы и продвижение в ещё открытых задачах отмечены раздельно. Независимая проверка доказательств и научного приоритета ещё не завершена.",
  "achievementBack":"← Обзор",
  "achievementCatalogue":"Все публикации",
  "achievementPageEyebrow":"ИЗБРАННЫЕ НАУЧНЫЕ РЕЗУЛЬТАТЫ",
  "achievementPageHeading":"Важные научные достижения",
  "achievementPageLead":"Точные экстремальные теоремы, продвижение в исторически исследуемых задачах и существенно суженный интервал открытой задачи о планарной квантовой нелокальности.",
  "achievementContextTitle":"Как читать заявления о результатах",
  "achievementContextText":"Ниже представлены результаты опубликованных рукописей CF Dependence. Точная формула для указанного класса объектов не смешивается с частичным улучшением или недоказанной гипотезой. Независимая проверка доказательств и исторического приоритета ещё не завершена; решения всех более широких классических задач мы не заявляем.",
  "achievementTocGhzExact":"GHZ: точно при n≥4",
  "achievementTocGhzThree":"GHZ: три участника",
  "achievementTocMixing":"Точная ковариация",
  "achievementTocMultilinear":"Мультлинейный вопрос 1985 года",
  "achievementTocProfile":"Универсальный CF-профиль",
  "achievementTocStability":"Точная устойчивость",
  "achievementStateExact":"Точный результат в указанном классе",
  "achievementStatePartial":"Строгие границы; точное значение открыто",
  "achievementStateRestricted":"Частичный ответ в ограниченном классе",
  "achievementGhzExactTitle":"Точный порог планарной GHZ-нелокальности при n ≥ 4",
  "achievementGhzExactDescription":"В работе выведена замкнутая формула оптимального порога локальной модели для GHZ-корреляций в плоскости XY при произвольных конечных наборах углов измерения и рассмотрении полных корреляций.",
  "achievementExample":"Пример",
  "achievementGhzExactImportance":"В отличие от численных оценок для конечных наборов измерений, это формула для оптимизации по всем наборам в указанной модели полных корреляций. Работа Designolle–Vértesi–Pokutta (2024) содержала строгие границы, но не эту общую аналитическую формулу.",
  "achievementGhzExactScope":"Область применимости: планарные XY-измерения и полные корреляции. Речь не обо всех неравенствах Белла или произвольных измерениях. Независимое ревью доказательства и исторического приоритета пока не завершено.",
  "achievementReadP04":"P04 — серия публикаций (Zenodo) ↗",
  "achievementReadDvp":"Designolle–Vértesi–Pokutta (2024) ↗",
  "achievementGhzThreeTitle":"GHZ для трёх участников: узкий интервал и гипотеза о точной формуле",
  "achievementGhzThreeDescription":"Для трёх участников точное значение пока не доказано. Статья даёт новую нижнюю границу из конечногармонического неравенства Белла и аналитическую верхнюю границу из явной локальной модели на основе меандров и функции Мёбиуса.",
  "achievementGhzThreeComparison":"Обе границы для порога видимости строже интервала 0.49129–0.49143, опубликованного Designolle–Vértesi–Pokutta в 2024 году. Ширина оставшегося интервала для κ₃ составляет лишь около 0.01775% его верхней границы.",
  "achievementGhzThreeConjecture":"Гипотеза: верхняя граница точна, κ₃ = 105ζ(3)/(2π³). Равенство пока не доказано.",
  "achievementGhzThreeProof":"Нижняя граница основана на аналитической редукции и 272 воспроизводимых рациональных неравенствах сертификата K7. Это компьютерно-ассистированное доказательство, но не независимая внешняя рецензия.",
  "achievementGhzThreeZeta":"При построении двойственного функционала Белла возникают арифметические осцилляции, связанные с функцией Мёбиуса и нулями дзета-функции Римана. Это не означает эквивалентности гипотезы о κ₃ гипотезе Римана.",
  "achievementMixingTitle":"Оптимальная ковариационная константа при сильном перемешивании",
  "achievementMixingDescription":"Для ограниченных комплексных случайных величин, измеримых относительно двух σ-алгебр, P04 доказывает точный коэффициент ковариационного неравенства через классический коэффициент сильного перемешивания α.",
  "achievementMixingHistory":"В литературе известна историческая граница Дворецкого 2π, обсуждаемая в Bradley–Bryc (1985). Константа 4√2 меньше; в P04 обоснована её точность конструкцией равенства. Для вещественных скаляров точная константа равна 4.",
  "achievementMixingScope":"Сравнение относится к одной нормировке коэффициента сильного перемешивания и ограниченных наблюдений. Исчерпывающий поиск более ранних эквивалентных точных результатов и независимое ревью ещё не завершены; мировой приоритет не заявляется.",
  "achievementReadBradley":"Bradley–Bryc (1985) ↗",
  "achievementMultilinearTitle":"Уточнение мультлинейных оценок и вопрос 1985 года",
  "achievementMultilinearDescription":"В 1985 году Bradley и Bryc указали, что коэффициенты их общего мультлинейного неравенства неоптимальны. В P04 получены точные вещественные и комплексные множители 2ⁿ и 2ⁿκₙ для естественного класса форм, принимающих вещественные значения на вещественных аргументах.",
  "achievementMultilinearScope":"Существенное ограничение: исходная работа 1985 года допускает произвольные комплексные мультлинейные формы, а теорема P04 относится к более узкому классу. Поэтому старая задача в общей постановке не решена. Точный комплексный множитель для n=3 также остаётся открытым.",
  "achievementProfileTitle":"Универсальный профиль зависимости через характеристические функции",
  "achievementProfileDescription":"Экстремальная задача по совместным законам ограниченных комплексных величин сведена к явной формуле через заданные модули их средних. Это объединяет несколько задач факторизации характеристических функций.",
  "achievementProfileImportance":"Точная универсальная константа имеет значения C₂=1, C₃=2/√3, C₄=9/7. В соответствующем режиме экстремаль реализует общий симметричный знак; C_d возрастает к 2. Это доказанный точный профиль, но не заявление о решении независимо сформулированной вековой открытой проблемы.",
  "achievementReadP01":"P01 — серия публикаций (Zenodo) ↗",
  "achievementStabilityTitle":"Точная количественная устойчивость вблизи экстремальной зависимости",
  "achievementStabilityDescription":"P13 усиливает точное неравенство теоремой об устойчивости: если дефект зависимости близок к максимуму, совместное распределение близко ко всему семейству случаев равенства.",
  "achievementStabilityScope":"При d≥3, любом конечном p≥1 и достаточно малом дефиците Δ показатель степени в оценке Васерштейна оптимален даже после оптимизации фаз. Для структурированного отклонения с раздельным учётом положения и масс получен оптимальный порядок √Δ.",
  "achievementStabilityPriority":"Результат выделен за точный показатель устойчивости и экстремальную геометрию, а не как независимо подтверждённое решение старой внешней задачи.",
  "achievementReadP13":"P13 — серия публикаций (Zenodo) ↗",
  "achievementEditorialTitle":"Доказательства, новизна и приоритет",
  "achievementEditorialText":"Математически точный результат может требовать независимой проверки доказательства и сопоставления с предшествующей литературой. Ссылки выше ведут на опубликованные статьи и исторические источники. Приведённые категории отражают математические утверждения и их границы, а не подтверждают независимое рецензирование.",
  "achievementEditorialSecond":"Точная формула GHZ для трёх участников остаётся гипотезой. Широкая комплексная мультлинейная задача 1985 года не объявляется решённой. Без независимого proof-review и документального сопоставления приоритета мы не используем формулировку «впервые в мире решена давняя открытая проблема».",
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
  programmeBridge:"Публикации ниже раскрывают связанные части программы: точные неравенства, заданные маргинали и транспорт, алгебру, гармонические методы восстановления и статистику.",
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
  newsLabel:"ИСТОРИЯ ВЫПУСКОВ",updatesHeading:"Что изменилось",
  updatesInfo:"Только подтверждённые публичные изменения. Резервирование DOI и внутреннее ревью не означают публикацию.",
  authorNav:"Об авторе",authorLabel:"ИССЛЕДОВАТЕЛЬ",authorHeading:"Об авторе",
  authorRole:"Независимый исследователь",
  aiDisclosureLabel:"ПРОЗРАЧНОСТЬ ИССЛЕДОВАНИЙ",aiDisclosureHeading:"Участие искусственного интеллекта",
  aiDisclosureText:"Исследования CF Dependence выполнялись автором совместно с системами искусственного интеллекта (ИИ). ИИ участвовал в математическом поиске, разработке и критическом анализе идей и доказательств, а также в подготовке рукописей. Системы ИИ не указаны в качестве соавторов. За опубликованные утверждения, доказательства и выводы отвечает автор.",
  aboutLabel:"ПРОЕКТ",aboutHeading:"О CF Dependence",
  aboutText:"Развивающаяся математическая программа, объединяющая экстремальную вероятность, зависимость при фиксированных маргиналях и алгебраические методы. Каталог ведёт к опубликованным версиям и общедоступным научным материалам.",
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
  renderUpdates($("news-items"),true);
}
function story(date, title, summary, source) {
  const article=node("article","news-item");
  const time=node("time",null,date); time.dateTime=date;
  const h=node("h3",null,title);
  const p=node("p",null,summary);
  article.append(time,h,p);
  if(source && source.startsWith("https://doi.org/")) {
    const a=node("a",null,source.slice("https://doi.org/".length)+" ↗");
    a.href=source;a.target="_blank";a.rel="noopener noreferrer";article.append(a);
  }
  return article;
}
function allUpdates() {
  const items=[...news.map(x=>({date:x.date,title:x.title[language],summary:x.summary[language],source:x.source||null}))];
  for (const p of papers) for (const c of p.changes||[]) {
    if (!DOI.test(c.doi) || !c.date) continue;
    items.push({date:c.date,title:p.code+" · "+p.title,summary:c.summary[language]||c.summary.en,source:"https://doi.org/"+c.doi});
  }
  return items.sort((a,b)=>b.date.localeCompare(a.date));
}
function renderUpdates(parent, includeSiteNews) {
  const events=includeSiteNews?allUpdates():[];
  parent.replaceChildren();
  if(!events.length){parent.appendChild(node("p","muted",COPY[language].newsEmpty));return;}
  for(const e of events)parent.appendChild(story(e.date,e.title,e.summary,e.source));
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
    const [a,b]=await Promise.all([fetch("data/papers.json",{cache:"no-store"}),fetch("data/news.json",{cache:"no-store"})]);
    if(!a.ok||!b.ok)throw new Error("Unable to load");
    const pdata=await a.json(), ndata=await b.json();
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
    news=Array.isArray(ndata.entries)?ndata.entries:[];
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
