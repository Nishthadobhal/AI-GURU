import Layout from "../components/Layout";
import "../styles/Dashboard.css";

function Dashboard() {
  return (
    <Layout>
      <div className="dashboard">

        <h1>Welcome, Nishtha 👋</h1>

        <p className="subtitle">
          Track your learning journey with AI Guru.
        </p>

        <div className="card-container">

          <div className="dashboard-card">
            <h3>Readiness</h3>
            <p>80%</p>
          </div>

          <div className="dashboard-card">
            <h3>Completed Topics</h3>
            <p>25</p>
          </div>

          <div className="dashboard-card">
            <h3>Weak Topics</h3>
            <p>3</p>
          </div>

          <div className="dashboard-card">
            <h3>Today's Goal</h3>
            <p>2 Hours</p>
          </div>

        </div>

      </div>
    </Layout>
  );
}

export default Dashboard;