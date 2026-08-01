import { useEffect, useState } from "react";
import { getRoadmap } from "../services/roadmapService";

function Roadmap() {

    const [roadmap, setRoadmap] = useState([]);
    const [title, setTitle] = useState("");
    useEffect(() => {

       const loadRoadmap = async () => {

    try {

        const studentId = localStorage.getItem("studentId");

        if (!studentId) {

            return;

        }

        const data = await getRoadmap(studentId);

        setRoadmap(data.weeks);
        setTitle(data.title);

    }

    catch (error) {

        console.log(error);

    }

};

loadRoadmap();

    }, []);

    const completedTopics = roadmap.filter(
        topic => topic.completed
    ).length;

    const progress = roadmap.length
        ? Math.round((completedTopics / roadmap.length) * 100)
        : 0;

    const currentTopic = roadmap.find(
        topic => !topic.completed
    );

    return (

        <div className="min-h-screen bg-[#0D1117] text-white">

            {/* Header */}

            <div className="max-w-5xl mx-auto px-8 py-10">

                <h1 className="text-4xl font-bold">
                    🧠 AI Guru
                </h1>

                <p className="text-gray-400 mt-2">
                    Personalized Learning Roadmap
                </p>

            </div>


            {/* Progress Card */}

            <div className="max-w-5xl mx-auto px-8">

                <div className="bg-[#161B22] rounded-2xl p-6">

                    <div className="flex justify-between">

                        <div>

                            <p className="text-gray-400">
                                Learning Goal
                            </p>

                            <h2 className="text-2xl font-bold mt-2">
                                {title}
                            </h2>

                        </div>

                        <div>

                            <p className="text-gray-400">
                                Progress
                            </p>

                            <h2 className="text-2xl font-bold mt-2 text-[#20E3B2]">
                                {progress}%
                            </h2>

                        </div>

                    </div>


                    <div className="mt-6 w-full h-3 bg-gray-700 rounded-full">

                        <div

                            className="h-3 bg-[#20E3B2] rounded-full"

                            style={{
                                width: `${progress}%`
                            }}

                        ></div>

                    </div>


                    {

                        currentTopic && (

                            <div className="mt-6">

                                <p className="text-gray-400">

                                    Current Topic

                                </p>

                                <h2 className="text-2xl font-semibold mt-2">

                                    📘 {currentTopic.topic}

                                </h2>

                            </div>

                        )

                    }

                </div>

            </div>


            {/* Timeline */}
            {/* Statistics */}

<div className="max-w-5xl mx-auto px-8 mt-8">

    <div className="grid grid-cols-1 md:grid-cols-3 gap-5">

        <div className="bg-[#161B22] rounded-xl p-5">

            <p className="text-gray-400">
                Completed
            </p>

            <h2 className="text-3xl font-bold text-green-400 mt-2">
                {completedTopics}
            </h2>

        </div>

        <div className="bg-[#161B22] rounded-xl p-5 hover:border hover:border-[#20E3B2] transition-all duration-300">

            <p className="text-gray-400">
                Remaining
            </p>

            <h2 className="text-3xl font-bold text-yellow-400 mt-2">
                {roadmap.length - completedTopics}
            </h2>

        </div>

        <div className="bg-[#161B22] rounded-xl p-5">

            <p className="text-gray-400">
                Total Topics
            </p>

            <h2 className="text-3xl font-bold text-[#20E3B2] mt-2">
                {roadmap.length}
            </h2>

        </div>

    </div>

</div>

            <div className="max-w-5xl mx-auto px-8 mt-10">

                <h2 className="text-2xl font-bold mb-8">

                    Learning Timeline

                </h2>

                {

                    roadmap.map((topic, index) => (

                        <div

                            key={index}

                            className="flex items-start gap-5"

                        >

                            {/* Left */}

                            <div className="flex flex-col items-center">

                                <div

                                    className={`

                                    w-8

                                    h-8

                                    rounded-full

                                    flex

                                    items-center

                                    justify-center

                                    font-bold

                                    ${

                                        topic.completed

                                        ?

                                        "bg-green-500"

                                        :

                                        index === completedTopics

                                        ?

                                        "bg-[#20E3B2] text-black"

                                        :

                                        "bg-gray-700"

                                    }

                                    `}

                                >

                                    {

                                        topic.completed

                                        ?

                                        "✓"

                                        :

                                        topic.week

                                    }

                                </div>

                                {

                                    index !== roadmap.length - 1 && (

                                        <div className="w-1 h-20 bg-gray-700"></div>

                                    )

                                }

                            </div>


                            {/* Right */}

                            <div className="flex-1 mb-10">

                                <div className="bg-[#161B22] rounded-xl p-5">

                                    <h3 className="text-xl font-bold">

                                        {topic.topic}

                                    </h3>

                                    <p className="text-gray-400 mt-3">

                                        {topic.description}

                                    </p>

                                </div>

                            </div>

                        </div>

                    ))

                }

            </div>
{/* Recommendation */}

<div className="max-w-5xl mx-auto px-8 mt-10">

    <div className="bg-[#161B22] rounded-2xl p-6">

        <h2 className="text-2xl font-bold mb-5">

            🎯 Today's Recommendation

        </h2>

        <p className="text-gray-300">

            Complete your current topic before moving to the next one.

        </p>

        <p className="mt-4 text-[#20E3B2]">

            Solve at least 5 practice questions today.

        </p>

    </div>

</div>
<div className="flex justify-center mt-10 mb-12">

    <button

        className="bg-[#20E3B2] text-black px-10 py-3 rounded-xl font-bold hover:scale-105 transition-all duration-300"

    >

        Continue Learning

    </button>

</div>
        </div>

    );

}

export default Roadmap;