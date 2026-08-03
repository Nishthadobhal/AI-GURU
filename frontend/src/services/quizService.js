import api from "./api";

// Get quiz by roadmap topic
export const getQuizByTopic = async (topicId) => {

    const response = await api.get(
        `/quizzes/topic/${topicId}`
    );

    return response.data;
};


// Submit Quiz
export const submitQuiz = async (data) => {

    const response = await api.post(
        "/quizzes/submit",
        data
    );

    return response.data;
};