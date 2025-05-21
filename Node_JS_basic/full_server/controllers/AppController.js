/**
 * This is the main controller for the application. It is the "hub" of the
 * application, in that virtually all requests for data or HTML from the
 * server pass through this controller.
*/
class AppController { 
  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!'); 
  }
}

export default AppController;
module.exports = AppController;