import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { getRoadmap } from "../services/roadmapService";
import {

    getQuizByTopic,

    submitQuiz

} from "../services/quizService";

import { getQuestionsByQuiz } from "../services/questionService";

function Quiz() {

    const location = useLocation();
    const [startTime, setStartTime] = useState(null);

    const [topicId, setTopicId] = useState(
    location.state?.topicId || null
);

    const [topicName, setTopicName] = useState(
    location.state?.topicName || ""
);

    console.log("Location State:", location.state);

    

    const [questions, setQuestions] = useState([]);
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [selectedOption, setSelectedOption] = useState(null);
const [answers, setAnswers] = useState({});
const [quizId, setQuizId] = useState(null);

const [result, setResult] = useState(null);

   const fetchCurrentTopic = async () => {

       try {

           const studentId = localStorage.getItem("studentId");

           const roadmap = await getRoadmap(studentId);

           const currentTopic = roadmap.weeks.find(
               topic => !topic.completed
        );

            if (currentTopic) {

                setTopicId(currentTopic.id);

                setTopicName(currentTopic.topic);

        }

    }

        catch (error) {

            console.log(error);

    }

};
    

    useEffect(() => {

        if (!topicId) {

            fetchCurrentTopic();

            return;

    }

        const loadQuiz = async () => {

           try {

               console.log("Topic ID:", topicId);

               const quizzes = await getQuizByTopic(topicId);

               console.log("Quizzes:", quizzes);

               if (!quizzes || quizzes.length === 0) {

                  alert("Quiz not found.");

                  return;

            }

               let selectedQuiz = null;

               for (const quiz of quizzes) {

                   const questionList =
                      await getQuestionsByQuiz(quiz.id);

                    if (questionList.length > 0) {

                        selectedQuiz = quiz;

                        setQuizId(quiz.id);

                        setQuestions(questionList);
                        setStartTime(Date.now());

                        break;

                }

            }

                if (!selectedQuiz) {

                    alert("No questions found.");

            }

        }

            catch (error) {

               console.log(error);

        }

    };

     loadQuiz();

}, [topicId]);
const handleSubmit = async () => {

    try {

        const studentId = Number(
            localStorage.getItem("studentId")
        );
        const endTime = Date.now();

        const timeTaken = Math.max(
           1,
           Math.round((endTime - startTime) / 60000)
);

        const payload = {

            student_id: studentId,

            quiz_id: quizId,


            time_taken_minutes: timeTaken,

            answers: Object.entries(answers).map(

                ([questionId, selectedAnswer]) => ({

                    question_id: Number(questionId),

                    selected_answer: selectedAnswer

                })

            )

        };

        console.log(payload);

        const response = await submitQuiz(payload);

        setResult(response);

    }

    catch (error) {

        console.log(error);

    }

};

if (result) {

    return (

        <div className="min-h-screen bg-[#0D1117] flex items-center justify-center text-white">

            <div className="bg-[#161B22] rounded-2xl p-10 text-center">

                <h1 className="text-4xl font-bold">

                    🎉 Quiz Completed

                </h1>

                <h2 className="text-5xl text-[#20E3B2] mt-6">

                    {result.score.toFixed(0)}%

                </h2>

                <p className="mt-5 text-xl">

                    Correct Answers

                </p>

                <p className="text-2xl mt-2">

                    {result.correct_answers}

                    /

                    {result.total_questions}

                </p>

            </div>

        </div>

    );

}

    return (

        <div className="min-h-screen bg-[#0D1117] text-white">

            <div className="max-w-4xl mx-auto px-8 py-10">

                <h1 className="text-4xl font-bold">

                    🧠 AI Guru Quiz

                </h1>

                <p className="text-gray-400 mt-2">

                    {topicName || "Test your understanding."}

                </p>

            </div>

            <div className="max-w-4xl mx-auto px-8">

                <div className="bg-[#161B22] rounded-2xl p-8">

                    <div className="flex justify-between">

                        <h2 className="text-xl font-bold">

                            Question {currentQuestion + 1}

                        </h2>

                        <p className="text-gray-400">

                            {questions.length === 0
                                ? "0 / 0"
                                : `${currentQuestion + 1} / ${questions.length}`}

                        </p>

                    </div>

                    <h3 className="text-2xl mt-8">

                        {questions.length > 0
                            ? questions[currentQuestion]?.question_text
                            : "🤖 AI Guru is preparing your quiz..."}

                    </h3>

                    <div className="mt-8 space-y-4">

                        {

                            questions.length > 0 &&

                            ["option_a", "option_b", "option_c", "option_d"].map(

                                (option) => (

                                    <button

                                        key={option}

                                       onClick={() => {
    console.log("Clicked:", option);
    setSelectedOption(option);

    setAnswers(prev => ({

        ...prev,

        [questions[currentQuestion].id]: option

    }));

}}

                                        className={`
                                            w-full
                                            text-left
                                            p-4
                                            rounded-lg
                                            transition

                                            ${

                                                selectedOption === option

                                                    ?

                                                    "bg-[#20E3B2] text-black"

                                                    :

                                                    "bg-gray-800 hover:bg-gray-700"

                                            }

                                        `}

                                    >

                                        {questions[currentQuestion][option]}

                                    </button>

                                )

                            )

                        }

                    </div>

                    <div className="flex justify-between mt-10">

                    <button

    onClick={() => {

        if (currentQuestion > 0) {

            const previousIndex = currentQuestion - 1;

            setCurrentQuestion(previousIndex);

            setSelectedOption(

                answers[questions[previousIndex]?.id] || null

            );

        }

    }}

    className="px-8 py-3 bg-gray-700 rounded-lg"

>

    Previous

</button>

                        <button

                            onClick={() => {

    if (!selectedOption) {

        alert("Please select an option.");

        return;

    }

    if (currentQuestion === questions.length - 1) {

        handleSubmit();

        return;

    }

    const nextIndex = currentQuestion + 1;

    setCurrentQuestion(nextIndex);

    setSelectedOption(

        answers[questions[nextIndex]?.id] || null

    );

}}

                        >

                           {
    currentQuestion === questions.length - 1

    ?

    "Submit Quiz"

    :

    "Next"
}

                        </button>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default Quiz;