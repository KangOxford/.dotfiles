Future Research Topics
=====

**************
Related Topics
**************

* **Optimal Execution**
   * Optimal liquidation or acqurization within 15-30 minutes with agent trained on the simulated environment.
* **Optimal Scheduling with Predicted Trading Volume**
   * In :doc:`_vwap_strategies`, split the task into smaller sizes according to the :doc:`_volume`.
* **Order-flow Generating**
   * Mathematical Perspective: Order flow as a general spatial point process
   * Time-series Forecasting for Order Flow
   * Order Flow Generating by Large Language Models
* Representation Learning
   * Representation Learning for the States/Observations
   * In the Optimal Execution, e.g. the all snapshots of limit order book in the past 30 seconds.
   * VAE, GAN and other encoder models.
* Price Impact Research through Market Clearing
   * Mathematical Perspective: Market clearing as a deterministic operator acting on the distributions of buy and sell orders.
   * Calculate the price impact without the assumption of impact function
* Indirect Market Impact
   * Agent's Impact on Triggering the Modification of other Agents' Actions
   * Different from the price impact, which is the direct maret impact.
* Agent Based Modelling/Simulation
   * Generative adversarial network approach simulation
   * Market Simulation
* Recover Trader's Reward Function
   * Recover Trader's Reward Function by Inverse RL
* Unsupervised Environment Design
   * Adversarial Learning by the differentiable environment


**************
Related Papers
**************

* Related Sections
   * Simulated Markets
   * Learning Trading Strategies
   * Forecasting Financial Data
* ICAIF2022
   * High Related
       * :doc:`_dyn`
       * :doc:`_learn`
       * :doc:`_cost`
   * Mid Related
       * Market Making under Order Stacking Framework: A Deep Reinforcement Learning Approach
       * Graph and tensor-train recurrent neural networks for high-dimensional models of limit order books
       * Computationally Efficient Feature Significance and Importance for Predictive Models
       * LaundroGraph: Self-Supervised Graph Representation Learning for Anti-Money Laundering
       * Deep Hedging: Continuous Reinforcement Learning for Hedging of General Portfolios across Multiple Risk Aversions
       * Efficient Calibration of Multi-Agent Simulation Models from Output Series with Bayesian Optimization
* ICAIF2021
   * High Related
      * :doc:`_towards_fully`
      * :doc:`_towards`
      * :doc:`_learning`
      * :doc:`_bit`
   * Mid Related
      * Deep Q-learning market makers in a multi-agent simulated stock market
      * FinRL: deep reinforcement learning framework to automate trading in quantitative finance
      * Sig-wasserstein GANs for time series generation
      * Agent-based markets: equilibrium strategies and robustness
      * Intelligent trading systems: a sentiment-aware reinforcement learning approach
      * High frequency automated market making algorithms with adverse selection risk control via reinforcement learning
   * Low Realted
      * An automated portfolio trading system with feature preprocessing and recurrent reinforcement learning
      * Monte carlo tree search for trading and hedging
      * Visual time series forecasting: an image-driven approach
      * Trading via selective classification
      * Timing is money: the impact of arrival order in beta-bernoulli prediction markets
      * An agent-based model of strategic adoption of real-time payments
      * FinRL-podracer: high performance and scalable deep reinforcement learning for quantitative finance
      * Stability effects of arbitrage in exchange traded funds: an agent-based model
* ICAIF2020
   * High Related
      * :doc:`_get`
      * :doc:`_multi`
      * :doc:`_deep`
   * Mid Related
      * A tabular sarsa-based stock market agent
      * Dynamic prediction length for time series with sequence to sequence network
* OMI Research Newsletter
   * fa
* Other related papers
   * :doc:`_stock`
   * :doc:`_generating`
   * :doc:`_deeprl`
   * :doc:`_many` 
   | from **OMI Research Newsletter – April 2023**



**************
Related Techniques
**************
* Transformers
   * Time Series Forecasting with Transformers
      * :doc:`_transformers_tsf`
   * Transformer in Low Signal-noise Ratio System
      * Sparse Transfomer: :doc:`_sparse_tf`
* Long Sequence Modelling
   * :doc:`_efficiently`
   * :doc:`_s5`
* Unsupervised Environment Design
   * :doc:`_ued`
* Behavior Cloning
   * :doc:`_bc`


**************
Related Issues
**************
* **Hard to generalize**. There might be several reasons jointly contribute to this situation:
   1. The **signal-to-noise ratio** of financial market data is much lower than that of other artificial intelligence fields.
   2. The financial market is not a closed system and will **evolve** on its own.
   3. The financial market is a derivative of the economy and therefore can be impacted by **external factors**.
