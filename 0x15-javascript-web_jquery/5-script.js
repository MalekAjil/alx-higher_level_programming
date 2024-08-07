$(function() {
	$("#add_item").click(function() {
		var item1 = $("<li></li>").text("Item");
		$("UL.my_list").append(item1);	
	});
});
