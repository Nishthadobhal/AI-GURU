import api from "./api";

// Get questions of a quiz

export const getQuestionsByQuiz = async (quizId) => {

    const response = await api.get(
        `/questions/quizzes/${quizId}/questions`
    );

    return response.data;
};