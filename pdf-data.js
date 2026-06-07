/**
 * ====================================================================
 * 📚 PDF資料室 データ定義ファイル (pdf-data.js)
 * ====================================================================
 * 
 * 【更新・管理手順】
 * 新しいPDF資料を追加・更新する場合は、以下の配列 (PDF_DATA) の先頭に
 * オブジェクトを追加してください。HTML側のソースコードを変更する必要はありません。
 * 
 * 【各項目の説明】
 * - title:       PDF資料のタイトル（カードに太字で表示されます）
 * - category:    カテゴリ名（自動で上部のフィルタボタンが生成されます）
 * - pdfUrl:      PDFファイルへのURL（WixメディアのURLや、サーバー上のパス）
 * - thumbnail:   サムネイル画像のURL（空文字 "" の場合は、デフォルトのPDFアイコンが表示されます）
 * - publishDate: 掲載日（YYYY-MM 形式。新しいものが自動で先頭に並びます）
 * - author:      著者名・発行者名（省略時は非表示になります）
 * - description: 資料の簡単な説明文（カードの下部に表示されます。省略可）
 */

const PDF_DATA = [
  // --- 1. 医局紹介・広報関連 ---
  {
    title: "専門研修プログラム詳細",
    category: "医局紹介",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_2f7f80ad6e40403e9b87323a4e90ab9b.pdf",
    thumbnail: "",
    publishDate: "2026-05",
    author: "浜松医科大学 耳鼻咽喉科・頭頸部外科",
    description: "専攻医向け後期専門研修プログラムの全体像、研修スケジュール、各関連病院の特色をまとめた詳細資料です。"
  },
  {
    title: "日耳鼻 教育・育成賞 受賞報告原稿",
    category: "表彰・受賞",
    pdfUrl: "", // 今後PDFが渡された際にURLを記載してください（例: "pdf/education_award.pdf"）
    thumbnail: "",
    publishDate: "2025-05",
    author: "耳鼻咽喉科・頭頸部外科教室",
    description: "学会から2年連続で「教育・育成功労賞」を受賞した際の記事および報告書の原稿PDF資料です。"
  },
  {
    title: "はんだ山の風 2025",
    category: "広報誌",
    pdfUrl: "", // 今後PDFのURLを記載してください
    thumbnail: "",
    publishDate: "2025-02",
    author: "静岡医科大学附属病院",
    description: "附属病院の広報誌「はんだ山の風」2025年版に掲載された、当科の活動および診療体制の紹介ページです。"
  },
  {
    title: "はんだ山の風 2024",
    category: "広報誌",
    pdfUrl: "", // 今後PDFのURLを記載してください
    thumbnail: "",
    publishDate: "2024-08",
    author: "静岡医科大学附属病院",
    description: "附属病院の広報誌「はんだ山の風」2024年版に掲載された、当科の紹介記事です。"
  },
  {
    title: "日耳鼻 新任教授のご挨拶",
    category: "医局紹介",
    pdfUrl: "", // 今後PDFのURLを記載してください
    thumbnail: "",
    publishDate: "2024-04",
    author: "三澤 清 教授",
    description: "三澤教授の着任にあたり、日本耳鼻咽喉科頭頸部外科学会誌等に寄稿された新任教授ご挨拶の原稿です。"
  },
  {
    title: "美蓄 New Wave 2024",
    category: "学会雑誌",
    pdfUrl: "", // 今後PDFのURLを記載してください
    thumbnail: "",
    publishDate: "2024-03",
    author: "免アレ感染学会誌",
    description: "免疫・アレルギー・感染関連学会誌に寄稿された原稿PDF資料です。"
  },
  {
    title: "附属病院リーフレット",
    category: "広報誌",
    pdfUrl: "", // 今後PDFのURLを記載してください
    thumbnail: "",
    publishDate: "2024-01",
    author: "静岡医科大学附属病院",
    description: "外来受診や紹介状のご案内など、当科の受診を検討される患者さん・ご家族向け紹介リーフレットです。"
  },

  // --- 2. 関連病院紹介PDF (affiliation.htmlから抽出) ---
  {
    title: "関連病院紹介：沼津市立病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_be7420c2969a475daa400a5e72f7cb07.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "沼津市立病院 耳鼻咽喉科",
    description: "沼津市立病院の耳鼻咽喉科・頭頸部外科における診療の特色、指導体制、研修医向けアピールポイントなどをまとめたPDF資料です。"
  },
  {
    title: "関連病院紹介：富士宮市立病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_47a6b3e21b364d7daf5e2718f04d2492.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "富士宮市立病院 耳鼻咽喉科",
    description: "富士宮市立病院における地域中核病院としての役割、一般耳鼻科診療および臨床研修の魅力をご案内する紹介PDF資料です。"
  },
  {
    title: "関連病院紹介：静岡済生会総合病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_453b1d709fec41cca6e9e90b294b424c.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "静岡済生会総合病院 耳鼻咽喉科",
    description: "静岡済生会総合病院の頭頸部外科・耳鼻咽喉科の診療体制、手術症例数、熱意あふれる指導体制についての資料です。"
  },
  {
    title: "関連病院紹介：焼津市立総合病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_832a7c647f0f4c268ee35a3830bc2c4a.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "焼津市立総合病院 耳鼻咽喉科",
    description: "志太榛原地区の基幹病院である焼津市立総合病院における、手術手技の習得と研修プログラムの特徴をまとめた資料です。"
  },
  {
    title: "関連病院紹介：藤枝市立総合病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_526700986dae437fa8828d11341cc5ed.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "藤枝市立総合病院 耳鼻咽喉科",
    description: "藤枝市立総合病院耳鼻咽喉科での初期・後期臨床研修プランや、豊富な手術経験が得られる診療環境をご紹介します。"
  },
  {
    title: "関連病院紹介：清水厚生病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_c2d2c143473846deae5b9cee7b724bb2.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "清水厚生病院 耳鼻咽喉科",
    description: "清水厚生病院の診療活動、地域住民を支える耳鼻咽喉科・アレルギー科医療の取り組みについて紹介しています。"
  },
  {
    title: "関連病院紹介：静岡厚生病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_127d81b4695f4e35ba5328f877f79398.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "静岡厚生病院 耳鼻咽喉科",
    description: "静岡厚生病院における、若手医師がプライマリケアから各種手術まで総合的に学べる環境や指導体制をご案内します。"
  },
  {
    title: "関連病院紹介：静岡県立こども病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_49980f0b42694f508c923646ef6e33a0.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "静岡県立こども病院 耳鼻咽喉科",
    description: "小児耳鼻咽喉科の専門的医療機関として、先天性疾患や難治性疾患に対する専門的アプローチと研修の特色をまとめた資料です。"
  },
  {
    title: "関連病院紹介：総合病院聖隷浜松病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_2897c3ad81674f5a8ad3adbe92d8bddb.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "聖隷浜松病院 耳鼻咽喉科・頭頸部外科",
    description: "トップクラスの手術症例数を誇る聖隷浜松病院の、頭頸部がん治療や高度中耳手術などの専門研修の魅力をまとめた資料です。"
  },
  {
    title: "関連病院紹介：浜松医療センター",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_b439390d5fcd47fe999666dfb5338707.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "浜松医療センター 耳鼻咽喉科",
    description: "浜松医療センター耳鼻咽喉科における高度救急医療と研修プログラム、指導医体制についてわかりやすく解説しています。"
  },
  {
    title: "関連病院紹介：総合病院聖隷三方原病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_011efd42ba824eb4a120d3d87af8ec39.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "聖隷三方原病院 耳鼻咽喉科",
    description: "聖隷三方原病院の耳鼻科における幅広い疾患群、嚥下治療などのチーム医療や当直等の研修環境についてご紹介します。"
  },
  {
    title: "関連病院紹介：遠州病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_ab389677d1b84c1e812880891c43d6cc.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "静岡県厚生連 遠州病院 耳鼻咽喉科",
    description: "浜松市中心部で地域医療に貢献する遠州病院の診療活動と、密着した医療活動・指導体制について紹介するPDF資料です。"
  },
  {
    title: "関連病院紹介：中東遠総合医療センター",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_9df876d627824ddd925b4926bdde63f6.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "中東遠総合医療センター 耳鼻咽喉科",
    description: "掛川市・袋井市地域の中核を担う中東遠総合医療センターでの頭頸部外科診療、若手医師の手術執刀・ステップアッププランをご案内します。"
  },
  {
    title: "関連病院紹介：磐田市立総合病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_deb5c6ad8fac47e0be8f249b8c486401.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "磐田市立総合病院 耳鼻咽喉科",
    description: "磐田市立総合病院の耳鼻咽喉科における多様な一般外来、救急症例、手術の執刀機会など若手専攻医向けの実務環境についての資料です。"
  },
  {
    title: "関連病院紹介：青山総合病院",
    category: "関連病院",
    pdfUrl: "https://25c240e4-6a91-46c1-9b35-a719bf4831fc.filesusr.com/ugd/2db1a0_e53da27a8127482e921170539b086049.pdf",
    thumbnail: "",
    publishDate: "2024-04",
    author: "青山総合病院 耳鼻咽喉科",
    description: "愛知県東部（豊川市・豊橋市等）の急性期医療を担う青山総合病院の、診療アピールポイントと研修体制についてのPDFです。"
  }
];
