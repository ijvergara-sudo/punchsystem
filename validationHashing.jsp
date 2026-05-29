<%/******
 This page create a connection to the Department database, and count all departments in the table department using the 
//ut.JAR.CPEN410.MySQLConnector class.**/
%>
<%//Import the ut.JAR.CPEN410 package for accessing the database %>
<%@ page import="ut.JAR.CPEN410.*"%>
<%//Import the java.sql package to use the ResultSet class %>
<%@ page import="java.sql.*"%>

<html>
		<head>
			<title>Your first web form!</title>
		</head>
<%
	 String userName=request.getParameter("username");
	 String passwd = request.getParameter("pin");

	if (userName.trim().equals("") || passwd.trim().equals("") ){
		//response.sendRedirect("login.html");%>
		<%=userName%>
		<br>
		<%=passwd%>
		bye!
		<%
	} else {%>

	
		<body>
			Hello!
		
		
			
	
	<%} 	%>
		</body>
	</html>