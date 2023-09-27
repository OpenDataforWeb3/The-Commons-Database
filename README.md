# The Commons Database
  
The Commons Database has emerged as a response to the critical need for enhanced transparency and data accessibility within the realm of project funding across diverse ecosystems.

Presently, application data in this domain remains compartmentalized, leaving grant administrators heavily reliant on applicant-provided information for assessing eligibility and risk. To address this challenge, the Commons Database has been developed to offer a comprehensive solution.

At its core, the platform collects and organises a wealth of data related to project digital representations through APIs, including those from Twitter, Github, and digital wallets. This data is systematically arranged into distinct tables for easy reference.

Notably, projects that have previously participated in stakeholder grant rounds are indexed within the database. Information about to their journey is automatically sourced from stakeholder systems or publicly available sources like on-chain registers.

The utility of this database extends to several critical use cases:

1. **Project Eligibility Analysis:** It facilitates a rigorous assessment of whether a project aligns with the necessary criteria to participate in grant rounds.

2. **Proof of Momentum:** A post-funding analysis of project activities aids in gauging its progress and trajectory.

3. **Risk and Anti-Fraud Analysis:** By examining project behavior across diverse platforms, it enables the identification and mitigation of potential risks.

The foundation of the Commons Database is built upon [Supabase](https://supabase.com/), an open-source alternative to Firebase, chosen for its capacity to provide storage, access, and other essential resources.

Automation plays a vital role in ensuring data accuracy. The platform leverages Github Actions to execute scheduled jobs that automate data retrieval and indexing, ensuring updates.
The scrips and yml. files for this process can be found on the .github file

For those seeking engagement and collaboration, the official communication hub resides on the [ODC Discord](https://discord.com/channels/1037443230993743902/1154807949089308703).  
Further insights into the project's roadmap and strategy documentation can be explored through the [Miro board](https://miro.com/app/board/uXjVMhnF9fo=/?share_link_id=636244343726).  

The Commons DB is a project idealized by [stefi](https://twitter.com/stefi_says), hosted on the OpenData Community Sandbox and developed in colaboration  with Gitcoin, Optmims and Octant 
