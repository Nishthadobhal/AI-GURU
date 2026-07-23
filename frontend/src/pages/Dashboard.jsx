import Layout from "../components/Layout";
import "../styles/Dashboard.css";
import DashboardCard from "../components/DashboardCard";
import api from "../services/api";
import { useState,useEffect } from "react";


function Dashboard() {

  const[readiness,setReadiness]=useState(0);
  const [progress, setProgress] = useState(0);

const [completedTopics, setCompletedTopics] = useState(0);

const [learningEvents, setLearningEvents] = useState(0);

const [weakTopics, setWeakTopics] = useState([]);

const [recommendation, setRecommendation] = useState([]);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {

    async function fetchDashboard() {
try {

    const response = await api.get("/dashboard/1");

    console.log(response.data);

    setReadiness(response.data.readiness);

    setProgress(response.data.progress);

    setCompletedTopics(response.data.completed_topics_count);

    setLearningEvents(response.data.total_learning_events);

    setWeakTopics(response.data.weak_topics);

    setRecommendation(response.data.recommendation);

} catch (error) {

    console.log(error);
  setError("Unable to load dashboard. Please try again.");

}
finally{

    setLoading(false);

}

    }

    fetchDashboard();

}, []);

if (loading) {

    return (

        <Layout>
<div className="loading">
    Loading Dashboard...
</div>

        </Layout>

    );

}

if (error) {

    return (

        <Layout>
<div className="error">
    {error}
</div>

        </Layout>

    );

}

  return (
    <Layout>
      <div className="dashboard">

        <h1>Welcome</h1>

        <p className="subtitle">
           Your AI-powered personalized learning dashboard.
        </p>

        <div className="card-container">

      <DashboardCard title="Readiness"  value={`${Math.round(readiness * 100)}%`}/>
<DashboardCard title="Progress" value={`${Math.round(progress * 100)}%`}/>
<DashboardCard title="Completed Topics" value={completedTopics} />
<DashboardCard title="Learning Events" value={learningEvents} />

        </div>
        <div className="bottom-section">

    <div className="weak-topics">

        <h2>Weak Topics</h2>

    <ul>

    {weakTopics.length === 0 ? (

        <li>No weak topics 🎉</li>

    ) : (

        weakTopics.map((topic, index) => (

            <li key={index}>{topic}</li>

        ))

    )}

</ul>

    </div>

  <div className="recommendation">

    <h2>AI Recommendation</h2>

    <ul>

        {recommendation.map((item, index) => (

            <li key={index}>{item}</li>

        ))}

    </ul>

</div>

</div>

      </div>
    </Layout>
  );
}

export default Dashboard;