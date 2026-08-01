import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "../pages/Landing";
import Onboarding from "../pages/Onboarding";
import Roadmap from "../pages/Roadmap";
import Quiz from "../pages/Quiz";
import MainLayout from "../components/layout/MainLayout";
import Login from "../pages/Login";


function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
       <Route path="/onboarding" element={<Onboarding />} />
        <Route element={<MainLayout />}></Route>
       <Route path="/roadmap" element={<Roadmap />} />
       <Route
    path="/quiz"
    element={<Quiz />}
/>
<Route
    path="/login"
    element={<Login />}
/>
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;