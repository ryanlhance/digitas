#!/usr/bin/env python3
"""Generates data.json for the Digitas fit-map page.
Single source of truth: edit this, run `python3 build_data.py`, and data.json
is rewritten. (Or just edit data.json directly — this is a convenience.)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Evidence (title + text shown to the reader) ----
evidence = json.loads(r'''
{
  "ev-sd-years": {
    "title": "7+ Years of Service Design",
    "text": "7+ years as a practicing service designer with an advanced degree in the specialty, but 13+ years designing how people move through complex products, services, and operations — including service design, innovation, and design strategy roles across multiple startups and Fortune 500 corporations; Delta Air Lines and Bayer."
  },
  "ev-client-years": {
    "title": "13 Years of Client-Facing Delivery",
    "text": "My career began with 6 years leading client work in film and TV + advertising and music videos. Since then, 7 years of client implementation, consulting, and stakeholder management across startups, nationwide franchises, Delta Air Lines, and Bayer."
  },
  "ev-scad": {
    "title": "Design Strategy M.A.",
    "text": "M.A. in Design Strategy from SCAD's De Sole School of Business Innovation — essentially an MBA crossbred with service design, built for intrapreneurship and using design thinking to influence decision making. My B.F.A. is from SCAD as well; business for film and television."
  },
  "ev-10industries": {
    "title": "Wide Industry Experience",
    "years": "14+ years experience",
    "text": "Experience across 10+ industries and hundreds of niche personas across unrelated service verticals — film and TV, agriculture, counseling, fitness, hospitality, education, logistics, sports entertainment. I learn fast, dive deep, and have a proven ability to onboard quickly to and lead in any business domain."
  },
  "ev-service-blueprint": {
    "title": "Service Blueprinting",
    "years": "7+ years experience",
    "text": "Built service blueprints at every scale from a 450-point blueprint for a startup's information architecture and executive decision making to a 20,000+ point global, enterprise level blueprint to identify service, product, technology, and operational gaps and opportunities at Bayer."
  },
  "ev-future-state": {
    "title": "Present State vs Future State",
    "years": "10+ years experience",
    "text": "I map the present state of an organization, business unit, or stakeholder journey to design the future state. The global blueprinting effort at Bayer existed to identify the present state of our tech stack and operational interactions and then make recommendations for future state: we delivered a present state map and a future state map. I did the same at Dryland Revival, mapping our current processes and then identifying new product and service opportunities for our customers and better ways of working for our teams."
  },
  "ev-journey": {
    "title": "Journey Mapping",
    "years": "7+ years experience",
    "text": "I have mapped journeys across startups, national franchises, and the Fortune 500. At Bayer I facilitated a global journey mapping effort spanning North America, Europe, and Asia-Pacific, 2,250 journey points across 27 teams, that cut environmental toxin risk 70% and raised workplace safety 30% within two quarters. At Dryland, the customer and employee journeys inside our 450 point blueprint became the source for our playbooks, org design, and project management system. I led the migration of Bayer's global, enterprise level blueprint from Miro to TheyDo so the journeys could be managed more accurately and dynamically."
  },
  "ev-systems-mapping": {
    "title": "Systems Mapping",
    "years": "13+ years experience",
    "text": "I build maps that help teams see the bigger picture and communicate and make decisions more efficiently. At Dryland Revival, I built a map with 100+ interaction points across all five departments. I have built comparative org charts that let a nationwide franchise see its restructure clearly enough to reorganize without a single layoff, current and future state organizational maps for entire Fortune 500 divisions, and the visual maps of crew, cast, and equipment that ran thousands of production days across six years in the film industry."
  },
  "ev-systems-thinking": {
    "title": "Systems Thinking",
    "years": "13+ years experience",
    "text": "I live in a constant state of mapping systems in my head. It is what allowed me to excel at the rapid, leadership-level decision making of being an Assistant Director on set in the film industry and helps me see consequences of business decisions that most others don't. When I walk into a room, a team, or a company, I have the system mapped in my head immediately. The blueprints, frameworks, and playbooks I design are made to help others act with the level of empathy their stakeholders need."
  },
  "ev-root-cause": {
    "title": "Root Cause Solutioning",
    "years": "13+ years experience",
    "text": "I'll spend an entire day on a single problem, because I know that resolving the system instead of the symptom saves days, weeks, or months of work later. And not just for me, but for entire teams, divisions, or organizations as a whole."
  },
  "ev-prototyping": {
    "title": "Prototyping",
    "years": "13+ years experience",
    "text": "Build context appropriate prototypes, low to high fidelity, to make ideas testable and accessible to feedback and usability. Some examples: agentic user personas built and validated inside a Fortune 500 before commercial AI tools existed, sustainable business model prototypes for Delta, and the Fans First experiences the Savannah Bananas scaled to global fame. Not to mention the rapid prototyping of sites, tools, maps, and apps in the AI era."
  },
  "ev-experience-design": {
    "title": "Experience Design",
    "years": "13+ years experience",
    "text": "I have been designing experiences professionally for over a decade. At the end of six years in the entertainment industry, I helped develop and execute the prototype \"Fans First\" experience that became the standard the Savannah Bananas then scaled to global fame. Before that, I employed experience design principles to innovate on decades old traditions as Program Director of a 1,500 person summer camp, and taught those principles to the next generation of camp leaders. Since then, I designed multi-stakeholder experiences at Delta Air Lines and Campus Carriers, lead the end-to-end farmer experience at Bayer across marketing, product, and portal surfaces, and employee and customer experiences at Bayer, Dryland Revival, and the national franchises I work with at AGS."
  },
  "ev-product-lead": {
    "title": "End-to-End Product Leadership",
    "years": "7+ years experience",
    "text": "UX Lead on Bayer's end-to-end customer site rebuild, acting as the design side Product Manager — from the public marketing pages through the post log in customer portal — driving a 35% increase in product and service opportunities and leading user acceptance testing across the North American user base."
  },
  "ev-tech-blueprint": {
    "title": "Tech Stack Blueprinting",
    "years": "7+ years experience",
    "text": "Bayer's global enterprise blueprinting effort was tech stack blueprinting at the largest possible scale: mapping the present state of every tech stack, persona, and operational interaction across multiple countries, then delivering future state recommendations that exposed redundant systems and unserved gaps. At Dryland, the 450 point blueprint drove the design and redesign of our entire tech stack, from the original ClickUp buildout to a Monday.com rebuild and the Zapier automations connecting it all. I still do this for clients today, including the end-to-end service blueprint and strategic recommendations that determined a hospitality franchise's tech stack roadmap for multi-location build outs."
  },
  "ev-discovery": {
    "title": "Research & Discovery",
    "years": "7+ years experience",
    "text": "Discovery is where I start every engagement and conversation. Masters level training + 7 years of real world experience in ethnographic field research, stakeholder interviews, contextual inquiry, and journey mapping to turn workforce challenges into actionable solutions."
  },
  "ev-insights": {
    "title": "Prioritization via Insights",
    "years": "13+ years experience",
    "text": "As a strategist, I prioritize actions and roadmaps via active analysis. This is a muscle that has been being trained since running film sets and having to make significant, long term decisions live in the moment. I was then given the tools and additional frameworks in grad school where my research and prioritization skillsets were trained intentionally. At Bayer, ethnographic user discovery overturned product decisions external consultancies had built from business stakeholder input alone. At Delta, passing our concepts through a business model canvas reset the entire direction of the engagement. At Dryland, interviews with team leads redirected employee retention efforts, and now I guide executive teams in efforts that affect their entire company."
  },
  "ev-research-tools": {
    "title": "Research & Analytics Tools",
    "years": "7+ years experience",
    "text": "Masters level training + 7 years of real world experience in research and analysis as well as their most premium tools: MAXQDA for qualitative coding, DisplayR and QuestionPro for survey and quantitative analysis, plus the discovery toolkit of interviews, contextual inquiry, and ethnographic field research behind them."
  },
  "ev-validation": {
    "title": "Testing & Validation",
    "years": "7+ years experience",
    "text": "Led User Acceptance Testing across a Fortune 500's North American user base, built agentic personas validated above 80% by 20+ year subject matter experts that cut UAT failures, and always run usability and prototype testing to pressure test ideas before they ship."
  },
  "ev-metrics": {
    "title": "Metrics Design",
    "years": "7+ years experience",
    "text": "Masters level training in metric determination: designing the right success metrics for the situation, then measuring against them. Fluent in OKRs, KPIs, NPS, adoption rate, time to launch, and satisfaction. Decision criteria that anchored client adoption logic in my work with Delta, the Franchise Criteria Canvas and priority matrices that gave a nationwide franchise an agreed standard for franchisee decisions, the SME validation threshold that gated Bayer's agentic personas before teams were allowed to rely on them, and the performance analytics, trackers, and dashboards Dryland ran on. Regularly measuring outcomes against the vision that was set: a 35% lift in product and service opportunities, a 30% rise in workplace safety, and 2% to 26% platform adoption in two months.\n\n---"
  },
  "ev-gtm": {
    "title": "Go-to-Market & Offer Design",
    "years": "7+ years experience",
    "text": "Structured the offer and go-to-market strategy for seven intrapreneurial and entrepreneurial ventures: an internal agentic tool at Bayer, sustainable products at Delta Air Lines, an education as a service line with Campus Carriers, the business model for Dryland Revival, multiple successful leadership practices, my franchise consulting business. Formal training in business modeling and GTM strategy (M.A. program at SCAD), niche and offer design (Traffic & Funnels) and offers, leads, and business models (Acquisition.com). I take an opportunity from value proposition to packaging, and into a working product or service."
  },
  "ev-bizmodel": {
    "title": "Business Model Design",
    "years": "7+ years experience",
    "text": "Designed business models, tech stacks, and service models across many engagements: agentic tools within Bayer, sustainable business models for Delta's obsolete beverage carts, a construction-science startup's operating model, a B2B2C education as a service for Campus Carriers, a hospitality franchise's multi-location tech roadmap, and five personal ventures grown to profitability."
  },
  "ev-advising": {
    "title": "Strategic Advising",
    "years": "13+ years experience",
    "text": "My strategic advising goes back to film and TV, where the producer's first job is advising the client on their own vision: what is actually possible within the timeline and budget, and what it will take to get there. Since then: primary client contact for Delta Air Lines leading a sustainability marketing effort, almost eight years of coaching leaders through my own practices, and advising for franchisees and franchisors today."
  },
  "ev-change": {
    "title": "Change Management",
    "years": "12+ years experience",
    "text": "Drove change and adoption in resistant systems my entire career: from navigating day-to-day and hour-by-hour changes on film sets to innovating decades old traditions while keeping the soul of the experience at a 1,500 person summer camp, including a decade old training program replaced with modern methods, creating a 67% year over year retention lift; a nationwide counseling franchise led through restructuring across states without a single layoff; a startup org redesign that doubled revenue and quadrupled headcount; moving a construction field crew into modern technology in the context of a phone based project management system; and leading a Fortune 500 AI platform from 2% to 26% adoption in two months."
  },
  "ev-entrepreneur": {
    "title": "Entrepreneurial Mindset",
    "years": "12+ years experience",
    "text": "Grew multiple ventures from zero to profitable exit — a bicycle rental venture in college, a construction sciences startup in Washington, a community based product business and vending machine business in Atlanta, and multiple consulting and coaching practices working with teens and young professionals to franchises and community and business leaders."
  },
  "ev-startup-os": {
    "title": "Startup Operating Systems",
    "years": "9+ years experience",
    "text": "I have built the operating systems of two startups. At Campus Carriers, a university logistics startup, I ran the largest location — a 20 truck fleet, a 100,000 square foot warehouse, and 200+ seasonal staff. I built the operational playbook covering recruiting, onboarding, training, scheduling, inventory, and safety that drove a 60% resource reduction and propagated across the other partner campuses, while pioneering an education as a service revenue line on top of it. At Dryland Revival, as co-founder and second hire, I built the operating system as we grew from one client to a profitable exit: playbooks, hiring funnel, project management system and tech stack, and the org redesign that let the CEO focus on his highest leverage work."
  },
  "ev-rd-lab": {
    "title": "Personal R&D Lab",
    "years": "16+ years experience",
    "text": "My personal life is a constantly running R&D lab — I've been ramping on a new technology at least once a quarter since high school, and my current operating system pairs agentic AI workflows with a digital brain to extend what I can do. I love unfamiliar domains and emerging tech.\n\n---"
  },
  "ev-agile": {
    "title": "Agile Experience",
    "years": "4+ years experience",
    "text": "Worked inside agile product teams across four Bayer platforms: refined backlogs, aligned hundreds of technical stories to user needs, led user acceptance testing across the North American user base, then built out the scrum board — writing all the stories and leading scrum — for a legacy platform team.\n\n---"
  },
  "ev-workstreams": {
    "title": "Multiple Workstreams",
    "years": "13+ years experience",
    "text": "Like my time in the entertainment industry, summer camping, and consulting, my role at Bayer was constantly in flux. I started as the UX lead for the farmer experience, became a design strategist for the operations platforms, then lead strategist for the generative AI effort, turning a six month contract into 18 months by continuing to be useful. I ramp quickly on new problems."
  },
  "ev-concurrent": {
    "title": "Concurrent Project Management",
    "years": "10+ years experience",
    "text": "Owned film and TV productions end to end as the client's point of contact, delivering on time and on budget while running an average of six concurrent productions, peaking at ten to twelve multiple times. Currently managing multiple engagements with AGS."
  },
  "ev-engagement": {
    "title": "Engagement Ownership",
    "years": "13+ years experience",
    "text": "I lead multiple concurrent client engagements end to end, owning scoping, timeline, and delivery from discovery through handoff. This skillset developed in film and TV first, where our crew averaged six productions at a time and peaked between ten and twelve. I also owned multiple engagements with business stakeholders as a design leader at Bayer and Delta Airlines."
  },
  "ev-client-delivery": {
    "title": "End-to-End Client Delivery",
    "years": "13+ years experience",
    "text": "Six years in film and TV owning productions end to end as the client's point of contact, on time and on budget across roughly 50 productions, including a branded film for Hamilton Watches spanning 30+ crew, 20+ talent, eight locations, and ten-plus vendor partners. Then Delta, where I was the primary contact between client and team, presenting at corporate while translating business needs to the creative team in the studio. Today I own consulting engagements end to end for franchisors, franchisees, and service businesses, from scoping and discovery through implementation and adoption."
  },
  "ev-rampfast": {
    "title": "Rapid Domain Learning",
    "years": "13+ years experience",
    "text": "Joined into a Fortune 500 knowing nothing about agriculture and was shipping across four platforms within a year. Joined Dryland knowing nothing about construction sciences and grew the business to profitability within two years. Have done relevant and successful consulting work in 10+ unfamiliar domains."
  },
  "ev-live-decisions": {
    "title": "High Stakes Decision Making",
    "years": "13+ years experience",
    "text": "As an assistant director and production coordinator in the entertainment industry, my brain was the on-set hub for information, prioritization, and decision-making across 40 productions, coordinating thousands of crew, cast, and vendors live — and de-escalating the \"whatever can go wrong will go wrong\" situations."
  },
  "ev-crossfn": {
    "title": "Cross-Functional Leadership",
    "years": "13+ years experience",
    "text": "I have led across functions and disciplines my entire career. On film sets, every department head came to me as the hub for information, prioritization, and decision making across thousands of crew, cast, and vendors. At Delta, I led a cross-cultural team spanning eight countries and nine disciplines while owning budget, timelines, and the client relationship, presenting at corporate and translating business needs to the creative team in the studio. At Bayer, I aligned 27 teams that did not report to me across North America, Europe, and Asia-Pacific. At Dryland, all six teams ran on the operating systems I developed."
  },
  "ev-translator": {
    "title": "Cross Discipline Fluency",
    "years": "13+ years experience",
    "text": "Fluent in business, design, and engineering languages. I love translating business jargon to design requirements, engineering capabilities to business possibilities, and design visions to engineering roadmaps. This is the product and service version of what I did as a producer and assistant director in the entertainment industry in the first half of my career."
  },
  "ev-facilitation": {
    "title": "Workshop Facilitation",
    "years": "12+ years experience",
    "text": "I have practiced facilitation professionally for over a decade. Hundreds of design thinking workshops from 5 to 150 people at Bayer, where Miro selected me as the sole Enterprise Advocate for a company of ~100,000 people. Staff trainings, development programming, and multi-day events for a 250 person staff at one of the country's largest summer camps. Eight years of leadership retreats, cohorts, and group trainings through my own practices, from high school and college students to the men's work I facilitate today. And the working sessions I currently run with franchise corporate teams and franchisees."
  },
  "ev-speaking": {
    "title": "Public Speaking & Presentations",
    "years": "10+ years experience",
    "text": "Over a decade of live presentations, from pitch decks in Fortune 500 corporate rooms to multi-day retreats, scaled coaching programs, and live events for a 1,500-person camp. Comfortable commanding a room of five people to five thousand."
  },
  "ev-exec": {
    "title": "Executive Alignment",
    "years": "10+ years experience",
    "text": "At Bayer, I developed an agentic AI experience and sold it internally through months of workshops, demos, and one on one influencing before getting the greenlight to build. At Delta, I was the primary client contact, presenting status updates and pitch decks regularly to corporate. As a franchise consultant, I work directly with CEOs, executive teams, and franchisors. At Dryland, I was the CEO's first conversation and advisor on every major decision. The first half of my career in film was aligning clients and directors on what was actually possible within the timeline and budget."
  },
  "ev-storytelling": {
    "title": "Storytelling & Executive Narrative",
    "years": "10+ years experience",
    "text": "Ten years writing 20 to 50 pages a week of creative and business content, from user stories to executive strategy. As Delta's primary client contact I presented status updates and pitch decks in corporate rooms while translating business needs to the creative team, and I sold an agentic AI build to Bayer executives through months of workshops, demos, and one-on-one narrative."
  },
  "ev-writing": {
    "title": "Strategic Writing & Documentation",
    "years": "10+ years experience",
    "text": "Built upon a practice of writing 20 to 50 pages a week, I have delivered hundreds of scripts and character driven narratives, as well as hundreds of pages of strategic documentation, philosophical essays, user stories, and executive strategy. I authored Bayer's Universal Design Principles, adopted across every platform in the division, the Customer Data Platform strategy documentation that anchored vendor selection at the enterprise level, and the AI Strategy Playbook shipped in 20+ languages. Today I write the documentation depth that powers tool agnostic AI knowledge management."
  },
  "ev-psych": {
    "title": "Human Behavior & Psychology",
    "years": "12+ years experience",
    "text": "Gallup Certified Strengths Coach trained in behavior and relationship psychology. This guides my deep empathy for user behavior, and my ability to influence change without authority. Eight years of teaching emotional intelligence and social emotional learning professionally means I can read motivations, needs and expectations, and emotions as a professional expertise, not a personality trait. I use that background to shape desirability and adoption."
  },
  "ev-mentor": {
    "title": "Mentorship Experience",
    "years": "12+ years experience",
    "text": "Ran training and development for a 250 person camp staff, redesigning a program that lifted retention 67% year over year, am Gallup certified, trained leadership coach with almost eight years running my own coaching practice, and spent six years in film identifying underutilized talent, developing them through on set mentor matching, and enabling them to lead their own crews."
  },
  "ev-talent": {
    "title": "Talent Development",
    "years": "10+ years experience",
    "text": "Built individualized development plans across a 250 person camp staff, created a system for on set mentor matching in film that identified underused talent and launched them to lead their own crews, and design and facilitate leadership programming for the last eight years."
  },
  "ev-coaching": {
    "title": "Coaching",
    "years": "7+ years experience",
    "text": "Gallup Certified Strengths Coach trained in behavior and relationship psychology; almost eight years of facilitating leadership development in the context of empathy strategies and emotional intelligence professionally. Built a leadership development practice from scratch to five figure revenue months within six months, running and iterating workshops and facilitation opportunities since. I've coached hundreds of high school and college students through multi-month social-emotional learning and leadership programs, and hundreds of others through weekend retreats, cohorts, and high ticket 1:1 men's work, with custom tools for mental and emotional processing developed in line with my systems and design thinking background."
  },
  "ev-retention": {
    "title": "Team Retention",
    "years": "10+ years experience",
    "text": "I build teams that stick around. Some stats: roughly 95% crew retention across six years in film, a 67% year-over-year retention lift at a 250 staff summer camp, and a startup hiring funnel that delivered 100% season-long retention of the individuals who moved through it."
  },
  "ev-adoption": {
    "title": "Tool and AI Adoption",
    "years": "10+ years experience",
    "text": "Adoption is a design problem. At Bayer, I took a Fortune 500's internal AI platform from 2% to 26% adoption in two months, by treating it as a competence problem rather than a trust problem. Beyond that, I developed an agentic persona service that multiple anti-AI teams started using daily, a project management system that construction field crews actually used on their phones, the migration of Bayer's global blueprint from Miro to TheyDo that matured design thinking across the enterprise through ease of discovery for customer journey maps, and currently lead teams from Notion, Dropbox, and Google Drive into tool agnostic markdown systems that increases their AI usage. This passion started in the film industry where I led the adoption of on-set and pre-production technologies across teams and departments."
  },
  "ev-agents": {
    "title": "Building AI Agents",
    "years": "3+ years experience",
    "text": "Pioneered an agentic persona service at Bayer in 2023, before commercial agents were available. I built AI models of users our design team couldn't otherwise reach, wired into Microsoft Teams before commercial AI integrations existed for the company's stack. The workflow produced high fidelity user representations rapidly, validated by SMEs above 80% accuracy, and significantly reduced UAT failures across the teams that used them. That was over 3 years ago. Imagine what I can do with your data and Claude's newest features."
  },
  "ev-ai-strategy": {
    "title": "AI Product Strategy",
    "years": "3+ years experience",
    "text": "Led product strategy on the build out and adoption of Bayer's internal LLM platform pre-AI-boom, impacting design and product decisions and leading user testing. That work continues today as the core of my consulting practice. I build agentic, tool agnostic knowledge systems for creative and operational teams, design the prompt, workflow, and rule configurations they run on, and treat retrieval quality and human authored context as the leverage priority."
  },
  "ev-ai-training": {
    "title": "Global AI Training",
    "years": "3+ years experience",
    "text": "Authored Bayer's AI Strategy Playbook and led its global dissemination in 20+ languages to thousands of internal users across business, engineering, design, and HR — training entire departments of the business from Indonesia to Brazil in a single quarter."
  },
  "ev-financials": {
    "title": "Financials Ownership",
    "years": "13+ years experience",
    "text": "Owned client communication, budgets, timelines, and resource management in film and TV for years, where a blown day meant hundreds of thousands to millions of dollars. Additionally have Masters level training in financial modeling. P&Ls, forecasting, income statements, balance sheets, cash flow modeling, scenario modeling, valuation modeling, pricing modeling, startup runway modeling, revenue modeling, and budgeting."
  },
  "ev-revenue": {
    "title": "New Revenue Lines",
    "years": "13+ years experience",
    "text": "I have pioneered new revenue lines across startups, franchises, and the Fortune 500. Developed a B2B2C education as a service line at Campus Carriers, owned end to end from primary market research through curriculum design, offer design, and pre-launch partnerships across seven partner universities. New service offerings designed and launched at Dryland Revival through a growth run that doubled revenue year over year for three years. Sustainable business models for thousands of Delta's obsolete beverage carts. An operations and marketing transformation at a physical health franchisee that opened the path to a second location. And my own ventures: a bicycle rental marketplace for a university, a community based product business grown to profitability, a vending machine business grown to profitability and exited, and multiple coaching and consulting practices grown to recurring five figure months."
  },
  "ev-tooling": {
    "title": "Tooling & Platforms",
    "years": "16+ years experience",
    "text": "Fluent across the tech stack I have built and shipped projects in: design and mapping (Miro, Mural, TheyDo), knowledge and docs (Notion, Obsidian), project management (Monday.com, ClickUp, Asana, Jira, Aha!, Motion, Profit.co), AI (Claude Code, Claude Cowork, the Claude API, ChatGPT and the OpenAI API, agentic tooling), research and analytics (MAXQDA, DisplayR, QuestionPro), commerce (Shopify), and the everyday collaboration tools (Microsoft 365, Google Suite, Slack, Zoom, Loom, Dropbox). I self train on unfamiliar enterprise software to the depth of evaluating vendor fit at least once a quarter."
  },
  "ev-portfolio": {
    "title": "Full Portfolio",
    "text": "Twelve public case studies across service blueprints, journey maps, systems maps, AI strategy, and UX — each one walks through the process, the deliverables, and the impact.",
    "link": "https://www.hance.work/"
  },
  "ev-pf-blueprint-global": {
    "title": "Global Enterprise Service Blueprint",
    "text": "Bayer's 20,000+ point global service blueprint mapping tech, personas, and interactions across countries to surface redundancies and gaps.",
    "link": "https://www.hance.work/Global-Enterprise-Level-Service-Blueprint-cd937db4cb344b318bae4c6d1e7ca9fa?pvs=25"
  },
  "ev-pf-blueprint-local": {
    "title": "Local Enterprise Service Blueprint",
    "text": "A focused enterprise service blueprint mapping a business's systems and interaction points end to end.",
    "link": "https://www.hance.work/Local-Enterprise-Level-Service-Blueprint-74f9ecfa9f4a4873be1b909a7f5e37d8?pvs=25"
  },
  "ev-pf-journey": {
    "title": "Global Journey Mapping Effort",
    "text": "A 27-team global journey map producing 2,250 journey points and new processes on a confidential European compliance project.",
    "link": "https://www.hance.work/Global-Journey-Mapping-Effort-228e643935ea43aab50ee95d8f56305f?pvs=25"
  },
  "ev-pf-eraf": {
    "title": "Systems Flow (ERAF) Map",
    "text": "A systems-flow map of 100+ interaction points that helped siloed teams see their role in the larger business — and kept employees who were ready to quit over 'bad communication.'",
    "link": "https://www.hance.work/Systems-Flow-ERAF-Map-74cfa7e910564777a9883a55f066d4f9?pvs=25"
  },
  "ev-pf-cdp": {
    "title": "Customer Data Platform Roadmap",
    "text": "The use cases and roadmap, built from the customer-experience perspective, that anchored a Fortune 500's Customer Data Platform vendor selection.",
    "link": "https://www.hance.work/Customer-Data-Platform-Roadmap-0d65a3c99943497e9c969160e33742a2?pvs=25"
  },
  "ev-pf-ai-roadmap": {
    "title": "A.I. Product Roadmap",
    "text": "Product roadmap for a Fortune 500's internal AI platform, defining the use cases and the path to adoption.",
    "link": "https://www.hance.work/A-I-Product-Roadmap-d042f4d986e5441bbb80b5e5ea4bd018?pvs=25"
  },
  "ev-pf-platform-playbook": {
    "title": "Platform Design Playbook",
    "text": "A reusable playbook for designing and standing up new platforms.",
    "link": "https://www.hance.work/Platform-Design-Playbook-838ea8da681f4577bce28f0ea7e30b67?pvs=25"
  },
  "ev-pf-genai-playbook": {
    "title": "Generative A.I. Playbook",
    "text": "The AI strategy playbook that drove adoption from 2% to 26%, shipped in 20+ languages to thousands of users.",
    "link": "https://www.hance.work/Generative-A-I-Playbook-bb68ca8c80d840e5be083136a0b88f92?pvs=25"
  },
  "ev-pf-personas": {
    "title": "A.I. Persona Prototypes",
    "text": "Agentic AI personas wired into Microsoft Teams — built before commercial AI integrations existed and launched across multiple company-wide platforms — so teams could interview user models they couldn't otherwise reach.",
    "link": "https://www.hance.work/A-I-Persona-Prototypes-43575337f52c4cecaf4fdd871e5aa41e?pvs=25"
  },
  "ev-pf-usertesting": {
    "title": "User Testing Strategic Recommendations",
    "text": "Using user research and testing to inform strategic product development on a supply chain platform.",
    "link": "https://www.hance.work/User-Testing-Strategic-Recommendations-9f073d6ea0bb4bd1bef08d176895dd10?pvs=25"
  },
  "ev-pf-legacyux": {
    "title": "Legacy Software UX Strategy",
    "text": "Restructured forms, progress indicators, and language to make a legacy platform more efficient and usable.",
    "link": "https://www.hance.work/Legacy-Software-UX-Strategy-e189dab0fccc4d088f0f8e2a22b009a9?pvs=25"
  },
  "ev-pf-prompt": {
    "title": "Prompt Engineering Strategic Design",
    "text": "A prompt engineering approach and template that let non-technical stakeholders across the company use generative AI effectively for the first time.",
    "link": "https://www.hance.work/Prompt-Engineering-Strategic-Design-40891c882c00477e936743a5d0657ddc?pvs=25"
  }
}
''')

# ---- The job description, as real prose with inline highlighted phrases ----
jd_prose = json.loads(r'''
[
  {
    "type": "h2",
    "text": "Overview"
  },
  {
    "type": "p",
    "segments": [
      "As ",
      {
        "b": "VP/Director, Experience Strategy"
      },
      ", your ",
      {
        "id": "p-cx-expertise",
        "text": "comprehensive digital strategy and consumer experience expertise",
        "evidence": [
          "ev-experience-design",
          "ev-sd-years",
          "ev-product-lead"
        ]
      },
      " will be essential to ",
      {
        "id": "p-strategic-leadership",
        "text": "provide strategic leadership on key client engagements",
        "evidence": [
          "ev-advising",
          "ev-engagement",
          "ev-client-delivery"
        ]
      },
      "."
    ]
  },
  {
    "type": "p",
    "segments": [
      "Rooted in ",
      {
        "id": "p-empathy",
        "text": "an in-depth and empathetic understanding of the consumer's current environment and ecosystem",
        "evidence": [
          "ev-systems-thinking",
          "ev-discovery"
        ]
      },
      " as well as ",
      {
        "id": "p-motivators",
        "text": "their priorities, motivators and pain points",
        "evidence": [
          "ev-psych",
          "ev-journey"
        ]
      },
      ", this pivotal role demands a focus on how to most effectively ",
      {
        "id": "p-gaps",
        "text": "solve for experience gaps between today's consumer experience and the desired future state",
        "evidence": [
          "ev-future-state",
          "ev-service-blueprint",
          "ev-pf-blueprint-global",
          "ev-pf-blueprint-local"
        ]
      },
      "."
    ]
  },
  {
    "type": "h2",
    "text": "Responsibilities"
  },
  {
    "type": "p",
    "segments": [
      "Day-to-day, your role will concentrate on ",
      {
        "id": "p-key-accounts",
        "text": "guiding strategy across key accounts",
        "evidence": [
          "ev-concurrent",
          "ev-engagement"
        ]
      },
      " while delivering industry-leading service, which includes:"
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-data-analysis",
        "text": "Analyzing a variety of data-centric resources, hacking data",
        "evidence": [
          "ev-research-tools",
          "ev-pf-cdp"
        ]
      },
      ", ",
      {
        "id": "p-behaviors",
        "text": "researching behaviors, looking at what people are doing and hypothesizing why",
        "evidence": [
          "ev-discovery",
          "ev-psych",
          "ev-insights"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-personas",
        "text": "Building consumer personas",
        "evidence": [
          "ev-pf-personas",
          "ev-discovery"
        ]
      },
      ", ",
      {
        "id": "p-journeys",
        "text": "identifying pain points and mapping experience journeys",
        "evidence": [
          "ev-journey",
          "ev-pf-journey"
        ]
      },
      " to ",
      {
        "id": "p-emerging",
        "text": "envision brand experiences across web, mobile, AI and other emerging interfaces",
        "evidence": [
          "ev-product-lead",
          "ev-ai-strategy",
          "ev-pf-ai-roadmap"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      "Assisting or ",
      {
        "id": "p-workshops",
        "text": "leading experience ideation workshops with Experience Design teams and clients; facilitating conversations",
        "evidence": [
          "ev-facilitation"
        ]
      },
      " and ",
      {
        "id": "p-champion-insights",
        "text": "championing powerful, unexpected insights to inspire creative solutions",
        "evidence": [
          "ev-insights",
          "ev-storytelling"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-briefs",
        "text": "Crafting Experience briefs",
        "evidence": [
          "ev-writing",
          "ev-storytelling"
        ]
      },
      "; with powerful, unexpected insights that inspire"
    ]
  },
  {
    "type": "li",
    "segments": [
      "Identifying cultural trends and ",
      {
        "id": "p-startup-culture",
        "text": "keeping a pulse on internet and start-up culture",
        "evidence": [
          "ev-rd-lab",
          "ev-entrepreneur",
          "ev-startup-os"
        ]
      },
      "; ",
      {
        "id": "p-pov",
        "text": "providing teams and clients with a point of view",
        "evidence": [
          "ev-advising",
          "ev-exec"
        ]
      },
      " on how it affects the way brands connect with people"
    ]
  },
  {
    "type": "li",
    "segments": [
      "Helping to ",
      {
        "id": "p-business-cases",
        "text": "build digital product and service business cases to validate commercial viability",
        "evidence": [
          "ev-bizmodel",
          "ev-gtm",
          "ev-financials"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-agency-partners",
        "text": "Partnering with key players across the agency",
        "evidence": [
          "ev-crossfn",
          "ev-translator"
        ]
      },
      " (Relationship Leads, Technology, Experience Design and other teams) to ",
      {
        "id": "p-growth",
        "text": "determine strategy needs, growth possibilities and opportunities",
        "evidence": [
          "ev-revenue",
          "ev-insights"
        ]
      },
      " to ",
      {
        "id": "p-future-experiences",
        "text": "bring competitively differentiated future experiences to life",
        "evidence": [
          "ev-agents",
          "ev-future-state",
          "ev-prototyping"
        ]
      }
    ]
  },
  {
    "type": "h2",
    "text": "Qualifications"
  },
  {
    "type": "p",
    "segments": [
      "This critically important role requires ",
      {
        "id": "p-depth",
        "text": "a depth of expertise (10-12 years; min 4-year college degree, Masters preferred)",
        "evidence": [
          "ev-client-years",
          "ev-scad"
        ]
      },
      ", including ",
      {
        "id": "p-track-record",
        "text": "a track record of impactful work experience",
        "evidence": [
          "ev-portfolio",
          "ev-10industries"
        ]
      },
      " and professional ingenuity — which means you are:"
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-marketer",
        "text": "A digital experience-savvy marketer",
        "evidence": [
          "ev-experience-design",
          "ev-gtm",
          "ev-product-lead"
        ]
      },
      " and ",
      {
        "id": "p-problem-solver",
        "text": "passionate problem-solver",
        "evidence": [
          "ev-root-cause"
        ]
      },
      " with an unstoppable ",
      {
        "id": "p-inspire-teams",
        "text": "drive to inspire teams and bring the best work to life",
        "evidence": [
          "ev-crossfn",
          "ev-mentor"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-analytical",
        "text": "A strong analytical thinker and translator with exceptional data-dexterity",
        "evidence": [
          "ev-research-tools",
          "ev-translator",
          "ev-insights"
        ]
      },
      ", including the ability to ",
      {
        "id": "p-usability",
        "text": "conduct validation-usability studies to uncover insights",
        "evidence": [
          "ev-validation",
          "ev-pf-usertesting"
        ]
      },
      " that drive experience strategy, design and implementation"
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-system-thinker",
        "text": "A system-thinker",
        "evidence": [
          "ev-systems-thinking",
          "ev-systems-mapping",
          "ev-pf-eraf"
        ]
      },
      " with a ",
      {
        "id": "p-sd-ux",
        "text": "strong background or practiced expertise in service design and UX methods",
        "evidence": [
          "ev-sd-years",
          "ev-service-blueprint",
          "ev-pf-legacyux"
        ]
      },
      ", supported by ",
      {
        "id": "p-tech-platforms",
        "text": "knowledge of technology platforms",
        "evidence": [
          "ev-tooling",
          "ev-tech-blueprint",
          "ev-pf-platform-playbook"
        ]
      },
      " and SEO"
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-strategic-partner",
        "text": "A strategic partner who illuminates unexpected insights",
        "evidence": [
          "ev-insights",
          "ev-advising"
        ]
      },
      " and ",
      {
        "id": "p-clarity",
        "text": "provides clarity on the role and expectations of a digital experience",
        "evidence": [
          "ev-product-lead",
          "ev-metrics"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      "A collaborator ",
      {
        "id": "p-agile",
        "text": "comfortable in agile- or sprint-based approaches",
        "evidence": [
          "ev-agile"
        ]
      },
      ", ",
      {
        "id": "p-realtime",
        "text": "willing to work in real time",
        "evidence": [
          "ev-live-decisions"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      "A team leader and relationship builder who can ",
      {
        "id": "p-senior-clients",
        "text": "provide an authoritative point of view with senior clients",
        "evidence": [
          "ev-exec",
          "ev-advising"
        ]
      },
      ", while ",
      {
        "id": "p-all-levels",
        "text": "fostering partnership and collaboration with all levels of the agency and its partners",
        "evidence": [
          "ev-crossfn",
          "ev-client-delivery"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      "An approachable manager with a ",
      {
        "id": "p-talent",
        "text": "strong history of team oversight and talent development",
        "evidence": [
          "ev-talent",
          "ev-retention"
        ]
      },
      "; ",
      {
        "id": "p-coach",
        "text": "known to coach, educate and grow junior talent",
        "evidence": [
          "ev-coaching",
          "ev-mentor"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      "An all-around seasoned professional with ",
      {
        "id": "p-communication",
        "text": "exceptional communication, organizational and time management skills",
        "evidence": [
          "ev-speaking",
          "ev-storytelling",
          "ev-concurrent"
        ]
      },
      ", and the ",
      {
        "id": "p-adapt",
        "text": "flexibility to adapt quickly to change",
        "evidence": [
          "ev-change",
          "ev-rampfast",
          "ev-workstreams"
        ]
      }
    ]
  },
  {
    "type": "li",
    "segments": [
      {
        "id": "p-genai",
        "text": "Familiarity with prompt-based interaction and commonly used generative AI tools",
        "evidence": [
          "ev-pf-prompt",
          "ev-pf-genai-playbook",
          "ev-agents"
        ]
      },
      " (e.g., ChatGPT, Google Gemini, DALL·E, Midjourney) is a plus, especially ",
      {
        "id": "p-genai-tasks",
        "text": "for tasks like ideation, research, or content generation",
        "evidence": [
          "ev-ai-training",
          "ev-pf-personas",
          "ev-adoption"
        ]
      }
    ]
  }
]
''')

data = {
  "meta": {
    "candidate": "Ryan Hance",
    "portfolio": "https://www.hance.work/",
    "note": "Pure renderer input. Edit copy here (or in build_data.py). Each highlighted phrase carries the evidence ids that back it; evidence is a shared dictionary."
  },
  "job": {
    "company": "Digitas",
    "role": "VP/Director, Experience Strategy",
    "employment": "",
    "location": "Boston, Massachusetts (Hybrid)",
    "url": "https://careers.publicisgroupe.com/jobs/152832",
    "tab_title": "Ryan Hance · Fit Map",
    "candidate_kicker": "Ryan Hance · Fit Map",
    "candidate_lede": "These are selected notes and resume points from Ryan Hance's career experience mapped to the actual Digitas job description.",
    "candidate_stat": "Hover over any underlined phrase and select it to see Ryan's experience related to the ask."
  },
  "evidence": evidence,
  "jd_prose": jd_prose
}

out = os.path.join(HERE, "data.json")
with open(out, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# quick self-check: every referenced evidence id exists
ids = set()
for b in jd_prose:
    for seg in b.get("segments", []):
        if isinstance(seg, dict) and "evidence" in seg:
            ids.update(seg["evidence"])
missing = [i for i in ids if i not in evidence]
unused = [k for k in evidence if k not in ids]
print("Wrote", out)
print("phrases:", sum(1 for b in jd_prose for s in b.get("segments", []) if isinstance(s, dict) and "id" in s))
print("evidence items:", len(evidence))
print("missing evidence refs:", missing or "none")
if unused:
    print("unused evidence (fyi):", unused)
