import api from "./api";

export const loginStudent = async (name) => {

    const response = await api.post("/login", {
        name
    });

    return response.data;
};