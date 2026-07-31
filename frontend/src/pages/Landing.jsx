import { useNavigate } from "react-router-dom";

function Landing() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-[#0D1117] text-white flex flex-col items-center justify-center px-6">

      <h1 className="text-5xl font-bold mb-4">
        🧠 AI Guru
      </h1>

      <p className="text-xl text-gray-300 text-center max-w-2xl mb-10">
        Your Personalized AI Learning Companion
      </p>

      <div className="grid md:grid-cols-3 gap-6 mb-12">

        <div className="bg-[#161B22] p-6 rounded-xl w-64 text-center">
          <h2 className="text-xl font-semibold mb-2">
            🛣 Personalized Roadmaps
          </h2>

          <p className="text-gray-400 text-sm">
            Get a roadmap designed specifically for your learning goals.
          </p>
        </div>

        <div className="bg-[#161B22] p-6 rounded-xl w-64 text-center">
          <h2 className="text-xl font-semibold mb-2">
            🤖 AI Mentor
          </h2>

          <p className="text-gray-400 text-sm">
            Learn concepts interactively with your AI mentor.
          </p>
        </div>

        <div className="bg-[#161B22] p-6 rounded-xl w-64 text-center">
          <h2 className="text-xl font-semibold mb-2">
            📊 Learning Analytics
          </h2>

          <p className="text-gray-400 text-sm">
            Track your learning progress and performance.
          </p>
        </div>

      </div>

      <button
        onClick={() => navigate("/auth")}
        className="bg-[#20E3B2] text-black px-8 py-3 rounded-lg font-semibold hover:scale-105 transition"
      >
        Get Started
      </button>

      <p className="mt-6 text-gray-400">
        Already have an account?{" "}
        <span
          onClick={() => navigate("/auth")}
          className="text-[#20E3B2] cursor-pointer"
        >
          Login
        </span>
      </p>

    </div>
  );
}

export default Landing;