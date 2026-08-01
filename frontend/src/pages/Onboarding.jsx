import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerStudent } from "../services/studentService";
import { generateRoadmap } from "../services/roadmapService";
import { createLearningGoal } from "../services/learningGoalService";

function Onboarding() {
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [goal, setGoal] = useState("");
  const [learningStyle, setLearningStyle] = useState("");

  const handleGenerateRoadmap = async () => {

  if (!name || !goal || !learningStyle) {
    alert("Please fill all fields.");
    return;
  }

  try {

    const studentData = {
      name,
      goal,
      learning_style: learningStyle,
    };

    // Step 1 : Register Student
    const student = await registerStudent(studentData);

    // Save student id
    localStorage.setItem("studentId", student.id);

   // Step 2 : Save Learning Goal

await createLearningGoal({

    student_id: student.id,

    goal_name: goal,

    level: "Beginner"

});

// Step 3 : Generate AI Roadmap

const roadmap = await generateRoadmap(

    student.id,

    goal

);
    // // Save roadmap
    // localStorage.setItem(
    //   "roadmap",
    //   JSON.stringify(roadmap)
    // );

    navigate("/roadmap");

  } catch (error) {
    console.log("Full Error:", error);

    if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Data:", error.response.data);
    }

    alert("Something went wrong.");
}

};
  return (
    <div className="min-h-screen bg-[#0D1117] flex items-center justify-center px-4">
      <div className="bg-[#161B22] w-full max-w-lg rounded-2xl p-8">

        <h1 className="text-4xl font-bold text-white text-center mb-2">
          Welcome to AI Guru
        </h1>

        <p className="text-center text-gray-400 mb-8">
          Tell us about yourself to generate your personalized roadmap.
        </p>

        <div className="space-y-5">

          <input
            type="text"
            placeholder="Full Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full p-3 rounded-lg bg-gray-800 text-white border border-gray-700 outline-none focus:border-[#20E3B2]"
          />

          <input
            type="text"
            placeholder="Learning Goal"
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
            className="w-full p-3 rounded-lg bg-gray-800 text-white border border-gray-700 outline-none focus:border-[#20E3B2]"
          />

          <select
            value={learningStyle}
            onChange={(e) => setLearningStyle(e.target.value)}
            className="w-full p-3 rounded-lg bg-gray-800 text-white border border-gray-700 outline-none focus:border-[#20E3B2]"
          >
            <option value="">Select Learning Style</option>
            <option value="Visual">Visual</option>
            <option value="Reading">Reading</option>
            <option value="Practical">Practical</option>
            <option value="Mixed">Mixed</option>
          </select>

          <button
            onClick={handleGenerateRoadmap}
            className="w-full bg-[#20E3B2] text-black py-3 rounded-lg font-semibold hover:opacity-90 transition"
          >
            Generate My Roadmap
          </button>

        </div>
      </div>
    </div>
  );
}

export default Onboarding;