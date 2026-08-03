import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginStudent } from "../services/loginService";

function Login() {

    const navigate = useNavigate();

    const [name, setName] = useState("");

    const handleLogin = async () => {

    if (!name) {

        alert("Please enter your name.");

        return;
    }

    try {

        const student = await loginStudent(name);

        localStorage.setItem(
            "studentId",
            student.id
        );

        localStorage.setItem(
    "student",
    JSON.stringify(student)
);

        navigate("/roadmap");

    } catch (error) {

        if (error.response?.status === 404) {

            alert(
                "Student not found. Please create an account."
            );

        } else {

            alert("Something went wrong.");

        }

    }

};

    return (

        <div className="min-h-screen bg-[#0D1117] flex items-center justify-center">

            <div className="bg-[#161B22] p-10 rounded-2xl w-[420px]">

                <h1 className="text-4xl text-white font-bold text-center">

                    Welcome Back 👋

                </h1>

                <p className="text-gray-400 text-center mt-3">

                    Login to continue your learning journey.

                </p>

                <input

                    type="text"

                    placeholder="Enter your name"

                    value={name}

                    onChange={(e) => setName(e.target.value)}

                    className="w-full mt-8 p-3 rounded-lg bg-gray-800 text-white outline-none"

                />

                <button

                    onClick={handleLogin}

                    className="w-full mt-6 bg-[#20E3B2] text-black py-3 rounded-lg font-bold"

                >

                    Login

                </button>

                <p className="text-center text-gray-400 mt-6">

                    New Student?

                </p>

                <button

                    onClick={() => navigate("/onboarding")}

                    className="w-full mt-3 border border-[#20E3B2] text-[#20E3B2] py-3 rounded-lg"

                >

                    Create Account

                </button>

            </div>

        </div>

    );

}

export default Login;