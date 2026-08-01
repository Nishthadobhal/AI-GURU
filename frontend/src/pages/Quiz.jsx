import { useState } from "react";
import { useLocation } from "react-router-dom";

function Quiz() {
    const location = useLocation();

const {
    topicId,
    topicName
} = location.state || {};
    const [currentQuestion] = useState(0);

    return (

        <div className="min-h-screen bg-[#0D1117] text-white">

            <div className="max-w-4xl mx-auto px-8 py-10">

                <h1 className="text-4xl font-bold">

                    🧠 AI Guru Quiz

                </h1>

                <p className="text-gray-400 mt-2">

                    Test your understanding.

                </p>

            </div>

            <div className="max-w-4xl mx-auto px-8">

                <div className="bg-[#161B22] rounded-2xl p-8">

                    <div className="flex justify-between">

                        <h2 className="text-xl font-bold">

                            Question {currentQuestion + 1}

                        </h2>

                        <p className="text-gray-400">

                            1 / 10

                        </p>

                    </div>

                    <h3 className="text-2xl mt-8">

                          {topicName}

                    </h3>

                    <div className="mt-8 space-y-4">

                        <button className="w-full text-left p-4 rounded-lg bg-gray-800 hover:bg-[#20E3B2] hover:text-black transition">

                            Option A

                        </button>

                        <button className="w-full text-left p-4 rounded-lg bg-gray-800 hover:bg-[#20E3B2] hover:text-black transition">

                            Option B

                        </button>

                        <button className="w-full text-left p-4 rounded-lg bg-gray-800 hover:bg-[#20E3B2] hover:text-black transition">

                            Option C

                        </button>

                        <button className="w-full text-left p-4 rounded-lg bg-gray-800 hover:bg-[#20E3B2] hover:text-black transition">

                            Option D

                        </button>

                    </div>

                    <div className="flex justify-between mt-10">

                        <button className="px-8 py-3 bg-gray-700 rounded-lg">

                            Previous

                        </button>

                        <button className="px-8 py-3 bg-[#20E3B2] text-black rounded-lg font-bold">

                            Next

                        </button>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default Quiz;