# 📋 Project Rules - new-ent-website

These are the development and content creation rules for the official portal site of the Department of Otorhinolaryngology/Head and Neck Surgery at Hamamatsu University School of Medicine. AI agents must strictly follow these rules when working within this workspace.

## 🛠️ Applicable Skills
- **Priority Skill**: `ent-brand-guidelines`
  - When modifying/adding designs or writing content (HTML, text, etc.), you must prioritize applying the instructions in the global `ent-brand-guidelines` skill.

## 🎨 Design System
- **Color Palette**: Do not use default Tailwind CSS colors (e.g., `blue-500`) directly. You must strictly use the predefined brand colors (`brand.blue` = `#1b6ca8`, `brand.teal` = `#0f9f9a`, `brand.navy` = `#102033`, etc.).
- **Typography**: Use `Noto Sans JP` for Japanese text and `Inter` for English text/fallbacks.
- **Animations**: Use the `.reveal` transition class combined with the scroll-based Intersection Observer script for fade-in animations on sections/cards.

## ✍️ Content Writing (Tone & Manner)
- **Output Language**: All final generated text, HTML copy, and PR announcements must be written in **Japanese**.
- **Polite Tone**: Use polite Japanese (**敬体/Keitai**: *~desu*, *~masu* form) as the standard.
- **Target Audience**: Medical students, training program candidates (interns/residents), and young physicians.
- **Tone Balance**: Maintain an academic yet approachable tone. Provide context or explanations when using technical medical jargon so it is accessible to junior students.
