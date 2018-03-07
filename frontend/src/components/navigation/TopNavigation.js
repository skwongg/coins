import React from 'react';
import PropTypes from 'prop-types'
import { Menu, Dropdown, Image, Icon, Container } from 'semantic-ui-react';
import { connect } from 'react-redux'
import { Link } from 'react-router-dom';
import gravatarUrl from 'gravatar-url';
import * as actions from '../../actions/auth';


const TopNavigation = ({ user, logout, hasBooks }) => {
  return (
    <Container fluid>
      <Menu secondary pointing>
        { user.token ?
          <Menu.Item as={Link} to='/dashboard'>Dashboard</Menu.Item> : null
        }
        {hasBooks && <Menu.Item as={Link} to='/coins'>Coins</Menu.Item>}

        <Menu.Menu position="right">
          {user.token ?
            (<Menu.Item onClick={() => logout()}> Logout </Menu.Item>
              ) : (<Menu.Item as={Link} to='/login'> Login </Menu.Item>
            )
          }
        </Menu.Menu>
      </Menu>
    </Container>
  )
}

TopNavigation.propTypes = {
  user: PropTypes.shape({
    email: PropTypes.string.isRequired
  }).isRequired,
  hasBooks: PropTypes.bool.isRequired,
  logout: PropTypes.func.isRequired
}

function mapStateToProps(state){
  return {
    user: state.user,
    hasBooks: 1 //#TODO: allBooksSelector(state).length > 0
  }
}

export default connect(mapStateToProps, { logout: actions.logout })(TopNavigation);
