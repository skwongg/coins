import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { Route } from 'react-router-dom';
import HomePage from './components/pages/HomePage';
import LoginPage from './components/pages/LoginPage';
import DashboardPage from './components/pages/DashboardPage';
import TokenVerificationPage from './components/pages/TokenVerificationPage';
import SignUpPage from './components/pages/SignUpPage';
import ForgotPasswordPage from './components/pages/ForgotPasswordPage';
import ResetPasswordPage from './components/pages/ResetPasswordPage';
import UserRoute from './components/routes/UserRoute';
import GuestRoute from './components/routes/GuestRoute';
import TopNavigation from './components/navigation/TopNavigation';


const App = ({location, isAuthenticated}) =>
<div>
  <div className="ui row">
    {isAuthenticated && <TopNavigation />}
  </div>
  <div className="ui container">

    <Route
      location={location}
      path="/"
      exact
      component={HomePage}
      />

    <Route
      location={location}
      path="/verify/:token"
      exact
      component={TokenVerificationPage}
      />

    <GuestRoute
      location={location}
      path="/login"
      exact
      component={LoginPage}
      />

    <GuestRoute
      location={location}
      path="/signup"
      exact
      component={SignUpPage}
      />

    <GuestRoute
      location={location}
      path="/forgot-password"
      exact
      component={ForgotPasswordPage}
      />

    <GuestRoute
      location={location}
      path="/reset-password/:token"
      exact
      component={ResetPasswordPage}
      />

    <UserRoute
      location={location}
      path="/dashboard"
      exact
      component={DashboardPage}
      />

  </div>
</div>
App.propTypes = {
  location: PropTypes.shape({
    pathname: PropTypes.string.isRequired
  }).isRequired,
  isAuthenticated: PropTypes.bool.isRequired
}

function mapStateToProps(state){
  return {
    isAuthenticated: !!state.user.email
  }
}
export default connect(mapStateToProps)(App);
