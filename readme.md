<h1 align="center" id="title">Multi Agent Customer Support</h1>

<h2>🚀 Project Overview</h2>

Our flow begins with a user's question. This will then be passed to the <strong>ManagerAgent</strong> and various other input fields as needed.

<h2>Multi-Agent Routing and Tool Utilization</h2>

The <strong>ManagerAgent</strong> serves as a task coordinator, intelligently delegating responsibilities to specialized agents. Upon receiving a user's question, it evaluates the input and determines whether to utilize the <strong>OrderLookupAgent</strong> or the <strong>FAQAgent</strong> as a tool.

Once a response is obtained from the selected agent, the <strong>ManagerAgent</strong> synthesizes the information into a clear and cohesive reply.

<h3>OrderLookupAgent</h3>

The <strong>OrderLookupAgent</strong> operates in tool mode, allowing it to be utilized as a resource by the <strong>ManagerAgent</strong>. It processes input provided by the <strong>ManagerAgent</strong> to fulfill specific tasks.

Equipped with its own set of capabilities, this agent can access tools to retrieve information about orders and products. By leveraging the AstraDB vector store, it efficiently looks up details based on their IDs.

<h3>Querying the Database</h3>

The two Astra DB tools seen here are used to query information from the products and orders collection. These are used as tools by the <strong>OrderLookupAgent</strong>.

By providing the <em>orderNumber</em> and <em>productId</em> fields as mandatory tool parameters (due to the !) it forces the agent to pass these values. They will then be used as fields to query rows in each collection.

<h3>FAQ Agent</h3>

The <strong>FAQAgent</strong> operates in tool mode, allowing it to be utilized as a resource by the <strong>ManagerAgent</strong>. It processes input provided by the <strong>ManagerAgent</strong> to fulfill specific tasks.

This agent utilizes RAG, where it is able to search for relevant information from our company's frequently asked questions database.

<h2>Vector DB & RAG</h2>

This component integrates <strong>AstraDB</strong> for storing and searching vectorized data, primarily for tasks like FAQ retrieval or RAG workflows. Here's how it works based on the specific values:

<ol>
  <li><strong>Authentication</strong>: The <strong>Astra DB Application Token</strong> is used to securely connect to AstraDB. This ensures only authorized access to the database.</li>
  <li><strong>Data Source</strong>: The component queries the customer database, specifically the FAQ collection, which contains pre-stored FAQs or knowledge base entries.</li>
  <li><strong>Search Input</strong>: The user’s query will be processed when passed to this field dynamically during runtime.</li>
  <li><strong>Embedding Configuration</strong>:
    <ul>
      <li>Text data is converted into vector representations using the <strong>Astra Vectorize</strong> feature.</li>
      <li>The embeddings are generated using Nvidia's <strong>NV-Embed-QA</strong> model, which is specialized for question-answer tasks.</li>
      <li>This ensures the query and stored data are in a comparable format for semantic search.</li>
    </ul>
  </li>
  <li><strong>Retrieval Process</strong>: When a query is input, AstraDB searches the vector store to find the most relevant matching documents based on vector similarity.</li>
  <li><strong>Results</strong>: The output is displayed in the <strong>Search Results</strong> section, providing relevant responses to the user query, such as specific FAQ answers or product details.</li>
</ol>

<h2>Parsing Data & Prompt Injection</h2>

When we retrieve data from the Astra DB vector store database, it will be in JSON format. In order to use these data in our prompt and pass it to our LLM/agent, we need to convert it to text.

We start by parsing the data and then pass it as a prompt variable to the prompt that gets sent to our agent. This way the agent can view the contextually relevant results from our DB and use them in its response.
