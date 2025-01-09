<h1 align="center" id="title">Multi-Agent Customer Support System</h1>

<h2>🚀 Project Overview</h2>
<p>This project implements a multi-agent system designed to handle customer support queries efficiently. The system utilizes a <strong>ManagerAgent</strong> to route tasks intelligently to specialized agents such as the <strong>OrderLookupAgent</strong> and <strong>FAQAgent</strong>. These agents interact with a vector database for information retrieval, ensuring accurate and timely responses to customer queries.</p>

<h2>System Architecture and Agent Workflow</h2>

<h3>Step 1: Receiving User Input</h3>
<ul>
  <li>The process begins when a user submits a question or query.</li>
  <li>The input is directed to the <strong>ManagerAgent</strong>, which acts as the central coordinator.</li>
</ul>

<h3>Step 2: Task Delegation by ManagerAgent</h3>
<ul>
  <li><strong>ManagerAgent</strong> evaluates the user's query to determine the appropriate course of action.</li>
  <li>It decides whether to delegate the task to the <strong>OrderLookupAgent</strong> or the <strong>FAQAgent</strong>.</li>
</ul>

<h3>Step 3: OrderLookupAgent Functionality</h3>
<ul>
  <li>When selected, the <strong>OrderLookupAgent</strong> processes the input to retrieve order or product information.</li>
  <li>It queries the <strong>AstraDB</strong> vector store using mandatory parameters such as <em>orderNumber</em> and <em>productId</em>.</li>
  <li>Utilizes AstraDB tools to search the <strong>products</strong> and <strong>orders</strong> collections for relevant details.</li>
</ul>

<h3>Step 4: FAQAgent Functionality</h3>
<ul>
  <li>If the <strong>FAQAgent</strong> is chosen, it leverages the Retrieval-Augmented Generation (RAG) model.</li>
  <li>The agent searches the FAQ database in <strong>AstraDB</strong> to find answers matching the user's query.</li>
  <li>It uses <strong>Astra Vectorize</strong> and <strong>NV-Embed-QA</strong> to convert text into vector representations for semantic search.</li>
</ul>

<h3>Step 5: Data Retrieval and Response Synthesis</h3>
<ul>
  <li>Once the relevant information is retrieved, the <strong>ManagerAgent</strong> synthesizes the data into a coherent response.</li>
  <li>The synthesized response is then sent back to the user, providing a clear and accurate answer to their query.</li>
</ul>

<h2>Key Components</h2>

<h3>Vector Database (AstraDB) and RAG Integration</h3>
<ol>
  <li><strong>Authentication</strong>: Secure connection to AstraDB using an application token.</li>
  <li><strong>Data Source</strong>: Queries target the FAQ collection or order/product data collections.</li>
  <li><strong>Search Input</strong>: Dynamic user queries are processed at runtime.</li>
  <li><strong>Embedding Configuration</strong>:
    <ul>
      <li>Text data is vectorized using Astra Vectorize and NV-Embed-QA models.</li>
      <li>Ensures comparable formats for effective semantic search.</li>
    </ul>
  </li>
  <li><strong>Retrieval Process</strong>: Vector similarity is used to find the most relevant documents.</li>
  <li><strong>Results</strong>: Output is presented in the Search Results section.</li>
</ol>

<h2>Data Parsing and Prompt Injection</h2>
<ul>
  <li>Retrieved data from AstraDB is in JSON format.</li>
  <li>Data is parsed and injected into prompts sent to the LLM/agents.</li>
  <li>This ensures contextually relevant information is used in generating responses.</li>
</ul>

<h2>Project Objective</h2>
<p>The objective of the Multi-Agent Customer Support System is to streamline customer support operations by employing specialized agents that interact with a vector database for precise information retrieval, thereby enhancing the efficiency and accuracy of customer query resolution.</p>
