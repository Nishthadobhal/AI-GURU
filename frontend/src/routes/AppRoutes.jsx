import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "../pages/Landing";
import Login from "../pages/Login";
import Onboarding from "../pages/Onboarding";
import Roadmap from "../pages/Roadmap";
import Quiz from "../pages/Quiz";
import Mentor from "../pages/Mentor";
import MainLayout from "../components/layout/MainLayout";

function AppRoutes() {

  return (

    <BrowserRouter>

      <Routes>

        {/* Public Routes */}

        <Route path="/" element={<Landing />} />

        <Route path="/login" element={<Login />} />

        <Route path="/onboarding" element={<Onboarding />} />

        {/* Layout Routes */}

        <Route element={<MainLayout />}>

          <Route
            path="/roadmap"
            element={<Roadmap />}
          />

          <Route
            path="/quiz"
            element={<Quiz />}
          />

          <Route path="/mentor" element={<Mentor />} />

        </Route>


      </Routes>

    </BrowserRouter>

  );

}

export default AppRoutes;