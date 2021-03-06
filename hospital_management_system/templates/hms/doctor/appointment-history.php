<?php
session_start();
error_reporting(0);
include('../config/database.php');
include('include/checklogin.php');
check_login();
if(isset($_GET['cancel']))
		  {
mysqli_query($con,"update appointment set doctorStatus='0' where id ='".$_GET['id']."'");
                  $_SESSION['msg']="Appointment canceled !!";
		  }
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Doctor | Appointment History</title>

		<link href="http://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" rel="stylesheet" type="text/css" />
		<link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="vendor/themify-icons/themify-icons.min.css">
		<link href="vendor/animate.css/animate.min.css" rel="stylesheet" media="screen">
		<link href="vendor/perfect-scrollbar/perfect-scrollbar.min.css" rel="stylesheet" media="screen">
		<link href="vendor/switchery/switchery.min.css" rel="stylesheet" media="screen">
		<link href="vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.min.css" rel="stylesheet" media="screen">
		<link href="vendor/select2/select2.min.css" rel="stylesheet" media="screen">
		<link href="vendor/bootstrap-datepicker/bootstrap-datepicker3.standalone.min.css" rel="stylesheet" media="screen">
		<link href="vendor/bootstrap-timepicker/bootstrap-timepicker.min.css" rel="stylesheet" media="screen">
		<link rel="stylesheet" href="assets/css/styles.css">
		<link rel="stylesheet" href="assets/css/plugins.css">
		<link rel="stylesheet" href="assets/css/themes/theme-1.css" id="skin_color" />
	</head>
	<body>
		<div id="app">
<?php include('include/sidebar.php');?>
			<div class="app-content">


					<?php include('include/header.php');?>
				<!-- end: TOP NAVBAR -->
				<div class="main-content" >
					<div class="wrap-content container" id="container">
						<!-- start: PAGE TITLE -->
						<section id="page-title">
							<div class="row">
								<div class="col-sm-8">
									<h1 class="mainTitle">Doctor  | Appointment History</h1>
																	</div>
								<ol class="breadcrumb">
									<li>
										<span>Doctor </span>
									</li>
									<li class="active">
										<span>Appointment History</span>
									</li>
								</ol>
							</div>
						</section>
						<!-- end: PAGE TITLE -->
						<!-- start: BASIC EXAMPLE -->
						<div class="container-fluid container-fullw bg-white">


									<div class="row">
								<div class="col-md-12">

									<p style="color:red;"><?php echo htmlentities($_SESSION['msg']);?>
								<?php echo htmlentities($_SESSION['msg']="");?></p>
									<table class="table table-hover" id="sample-table-1">
										<thead>
											<tr>
												<th class="center">#</th>
												<th class="hidden-xs">Patient  Name</th>
												<th>Specialization</th>
												<th>Consultancy Fee</th>
												<th>Appointment Date / Time </th>
												<th>Appointment Creation Date  </th>
												<th>Current Status</th>
												<th>Action</th>

											</tr>
										</thead>
										<tbody>
<?php
$sql=mysqli_query($con,"select users.firstName as fname,appointment.*  from appointment join users on users.id=appointment.userId where appointment.doctorId='".$_SESSION['id']."'");
$cnt=1;
while($row=mysqli_fetch_array($sql))
{
?>

											<tr>
												<td class="center"><?php echo $cnt;?>.</td>
												<td class="hidden-xs"><?php echo $row['fname'];?></td>
												<td><?php echo $row['doctorSpecialization'];?></td>
												<td><?php echo $row['consultancyFees'];?></td>
												<td><?php echo $row['appointmentDate'];?> / <?php echo
												 $row['appointmentTime'];?>
												</td>
												<td><?php echo $row['postingDate'];?></td>
												<td>
<?php if(($row['userStatus']==1) && ($row['doctorStatus']==1))
{
	echo "Active";
}
if(($row['userStatus']==0) && ($row['doctorStatus']==1))
{
	echo "Canceled by Patient";
}

if(($row['userStatus']==1) && ($row['doctorStatus']==0))
{
	echo "Canceled by you";
}
												?></td>
												<td >
												<div class="visible-md visible-lg hidden-sm hidden-xs">
							<?php if(($row['userStatus']==1) && ($row['doctorStatus']==1))
{ ?>


	<a href="appointment-history.php?id=<?php echo $row['id']?>&cancel=update" onClick="return confirm('Are you sure you want to cancel this appointment ?')"class="btn btn-transparent btn-xs tooltips" title="Cancel Appointment" tooltip-placement="top" tooltip="Remove">Cancel</a>|<a data-toggle="modal" data-target="#myModal">Open</a>
	<?php } else {

		echo "Canceled";
		} ?>
												</div>
												</td>
											</tr>
											<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
											  <div class="modal-dialog" role="document">
											     <div class="modal-content">
											      <div class="modal-header">
								                      <h5 class="modal-title" id="exampleModalLabel">Add Medical Notes</h5>
								                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
								                          <span aria-hidden="true">&times;</span>
								                      </button>
								                  </div>
								                  <div class="modal-body">

																			<style media="screen">
																				.list {
																				color: #555;
																				font-size: 14px;
																				padding: 0 !important;
																				width: 500px;
																				font-family: courier, monospace;
																				border: 1px solid #dedede;
																				}
																				.list li {
																				list-style: none;
																				border-bottom: 1px dotted #ccc;
																				text-indent: 25px;
																				height: auto;
																				padding: 10px;
																				text-transform: capitalize;
																				}
																				.list li:hover {
																				background-color: #f0f0f0;
																				-webkit-transition: all 0.2s;
																				-moz-transition:    all 0.2s;
																				-ms-transition:     all 0.2s;
																				-o-transition:      all 0.2s;
																				}

																						</style>
														<input name="bp" id="add_note" placeholder="Add Note" class="form-control wd-450" required="true">
														<button type="button" onclick="pushNotes()" class="btn btn-primary" >Add</button>
								           <form method="post" name="submit_notes">
														 <input type="text"  name="appointment_id" value= <?php echo $row["id"]; ?> hidden="hidden">
													<div class="lines"></div>
													<ul class="list" id="list">
														<?php
														$rowid=$row["id"];
														$all="";
														$sql2=mysqli_query($con,"select doc_notes  from appointment where id='$rowid'");
														while($row2=mysqli_fetch_array($sql2))
														{
															$all=$row2["doc_notes"];
														 ?>
														 <li><?php echo $row2["doc_notes"] ?></li>
													 <?php } ?>
													</ul>
													<textarea id="all_notes" name="all_notes" value="" hidden="hidden"><?php echo $all; ?></textarea>


											<div class="modal-footer">
											 <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
											 <button type="submit" name="submit_notes" class="btn btn-primary">Submit</button>

											  </form>
											</div>
											</div>
											</div>
											</div>
										</div>

											<?php

$cnt=$cnt+1;
											 }
											 if(isset($_POST['submit_notes']))
											 	{

													$app_id=$_POST["appointment_id"];

													$notes=$_POST['all_notes'];

											 	   $query=mysqli_query($con, "update appointment set doc_notes='$notes' where id= '$app_id'");

											 	  if ($query) {
											 	  echo '<script>alert("Notes Updated")</script>';
 													echo "<script>window.location.href ='appointment-history.php'</script>";
											 	}
											 	else
											 	  {
											 	    echo '<script>alert("Something Went Wrong. Please try again")</script>';
											 	  }


											 }


											 ?>



										</tbody>
									</table>
								</div>
							</div>
								</div>

						<!-- end: BASIC EXAMPLE -->
						<!-- end: SELECT BOXES -->

					</div>
				</div>
			</div>
			<?php  ?>
			<!-- start: FOOTER -->
	<?php //include('include/footer.php');?>
			<!-- end: FOOTER -->

			<!-- start: SETTINGS -->
	<?php include('include/setting.php');?>

			<!-- end: SETTINGS -->
		</div>
		<!-- start: MAIN JAVASCRIPTS -->
		<script src="vendor/jquery/jquery.min.js"></script>
		<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
		<script src="vendor/modernizr/modernizr.js"></script>
		<script src="vendor/jquery-cookie/jquery.cookie.js"></script>
		<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>
		<script src="vendor/switchery/switchery.min.js"></script>
		<!-- end: MAIN JAVASCRIPTS -->
		<!-- start: JAVASCRIPTS REQUIRED FOR THIS PAGE ONLY -->
		<script src="vendor/maskedinput/jquery.maskedinput.min.js"></script>
		<script src="vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.min.js"></script>
		<script src="vendor/autosize/autosize.min.js"></script>
		<script src="vendor/selectFx/classie.js"></script>
		<script src="vendor/selectFx/selectFx.js"></script>
		<script src="vendor/select2/select2.min.js"></script>
		<script src="vendor/bootstrap-datepicker/bootstrap-datepicker.min.js"></script>
		<script src="vendor/bootstrap-timepicker/bootstrap-timepicker.min.js"></script>
		<!-- end: JAVASCRIPTS REQUIRED FOR THIS PAGE ONLY -->
		<!-- start: CLIP-TWO JAVASCRIPTS -->
		<script src="assets/js/main.js"></script>
		<!-- start: JavaScript Event Handlers for this page -->
		<script src="assets/js/form-elements.js"></script>
		<script>
			jQuery(document).ready(function() {
				Main.init();
				FormElements.init();
			});
		</script>

		<script type="text/javascript">
		function pushNotes() {

		var w1 = document.getElementById('add_note').value;
		var inp=document.getElementById('all_notes')
		var li = document.createElement("li");
		li.innerText = w1;

		document.getElementById("list").appendChild(li);
		inp.value=inp.value+w1+"\n"
		document.getElementById('add_note').value=""
		}
		</script>
		<!-- end: JavaScript Event Handlers for this page -->
		<!-- end: CLIP-TWO JAVASCRIPTS -->
	</body>
</html>
