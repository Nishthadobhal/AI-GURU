import Layout from "../components/Layout";
import { useState } from "react";
import api from "../services/api";
import "../styles/Roadmap.css";

function Roadmap() {

    const [goal, setGoal] = useState("");

    async function generateRoadmap() {

        try {

            const response = await api.post("/ai-roadmap", {
                student_id: 1,
                goal: goal
            });

            console.log(response.data);

        } catch (error) {

            console.log(error);

        }

    }

    return (

        <Layout>

            <div className="roadmap">

                <h1>Learning Roadmap</h1>

                <p className="subtitle">
                    Track your learning journey.
                </p>

                <div className="roadmap-input">

                    <input
                        type="text"
                        placeholder="Enter your learning goal"
                        value={goal}
                        onChange={(e) => setGoal(e.target.value)}
                    />

                    <button onClick={generateRoadmap}>
                        Generate Roadmap
                    </button>

                </div>

            </div>

        </Layout>

    );

}

export default Roadmap;