import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { Route } from 'react-router-dom';
import HomePage from './components/pages/HomePage';
import LoginPage from './components/pages/LoginPage';
import UserRoute from './components/routes/UserRoute';
import GuestRoute from './components/routes/GuestRoute';
import TopNavigation from './components/navigation/TopNavigation';


const App = ({location, isAuthenticated}) =>
  <div className="ui container">
    {isAuthenticated && <TopNavigation />}

    <Route
      location={location}
      path="/"
      exact
      component={HomePage}
      />

    <GuestRoute
      location={location}
      path="/login"
      exact
      component={LoginPage}
      />


  </div>

App.propTypes = {
  location: PropTypes.shape({
    pathname: PropTypes.string.isRequired
  }).isRequired,
  isAuthenticated: PropTypes.bool.isRequired
}

function mapStateToProps(state){
  return {
    isAuthenticated: null
  }
}
export default connect(mapStateToProps)(App);
