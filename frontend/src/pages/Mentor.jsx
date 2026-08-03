import { useState } from "react";
import { askAIMentor } from "../services/aiMentorService";
import ReactMarkdown from "react-markdown";

function Mentor() {
const [loading, setLoading] = useState(false);
    const [messages, setMessages] = useState([
        {
            sender: "ai",
            text: "Hello! I'm your AI Mentor. I can help you with your roadmap, quizzes, learning progress, and programming questions. How can I help you today?"
        }
    ]);

    const [question, setQuestion] = useState("");
    
    const handleSend = async () => {

    if (!question.trim()) return;

    const studentId = Number(
        localStorage.getItem("studentId")
    );

    const userMessage = {
        sender: "user",
        text: question
    };

    setMessages(prev => [
        ...prev,
        userMessage
    ]);

    const currentQuestion = question;

    setQuestion("");
setLoading(true);  
    try {

        const response = await askAIMentor(
            studentId,
            currentQuestion
        );

        const aiMessage = {
            sender: "ai",
            text: response.answer
        };

        setMessages(prev => [
            ...prev,
            aiMessage
        ]);
setLoading(true);  
    }

    catch (error) {
setLoading(false);
        console.log(error);

        setMessages(prev => [
            ...prev,
            {
                sender: "ai",
                text: "Sorry, something went wrong."
            }
        ]);

    }

};

    return (

        <div className="min-h-screen bg-[#0D1117] text-white flex flex-col">

            <div className="bg-[#161B22] p-6 shadow-lg">

                <h1 className="text-3xl font-bold">
                    🤖 AI Mentor
                </h1>

            </div>

            <div className="flex-1 overflow-y-auto p-6 space-y-4">

                {
                    messages.map((message, index) => (

                        <div
                            key={index}
                            className={`flex ${
                                message.sender === "user"
                                    ? "justify-end"
                                    : "justify-start"
                            }`}
                        >

                            <div
                                className={`max-w-[70%] rounded-xl px-4 py-3 ${
                                    message.sender === "user"
                                        ? "bg-[#20E3B2] text-black"
                                        : "bg-[#161B22]"
                                }`}
                            >

                               <ReactMarkdown>
    {message.text}
</ReactMarkdown>

                            </div>

                        </div>

                    ))
                }
{
    loading && (

        <div className="flex justify-start">

            <div className="bg-[#161B22] rounded-xl px-4 py-3">

                AI is thinking...

            </div>

        </div>

    )
}



            </div>

            <div className="p-5 border-t border-gray-700 flex gap-3">

                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={(e) => {

    if (e.key === "Enter") {

        handleSend();

    }

}}
                    placeholder="Ask your AI Mentor..."
                    className="flex-1 rounded-lg px-4 py-3 bg-[#161B22] outline-none"
                />

                <button
    onClick={handleSend}
    className="bg-[#20E3B2] text-black px-6 rounded-lg font-semibold"
>
    Send
</button>

            </div>

        </div>

    );

}

export default Mentor;