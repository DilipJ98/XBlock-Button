function ButtonXBlock(runtime, element) {
  function displayRandomNumber(result) {
    $(".count", element).text(result.count);
  }

  var handlerUrl = runtime.handlerUrl(element, "random_generator");
  let obj = {
    hello: "world",
  };

  $("button", element).click((eventObject) => {
    $.ajax({
      type: "POST",
      url: handlerUrl,
      data: JSON.stringify(obj),
      success: displayRandomNumber,
    });
  });
}
