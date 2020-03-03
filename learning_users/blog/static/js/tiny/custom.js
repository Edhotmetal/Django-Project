
tinymce.init({
  selector: 'textarea',
  height: 500,
  menubar: 'image',
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace image visualblocks code fullscreen',
    'insertdatetime media table paste code help wordcount codesample code'
  ],
  codesample_languages: [
		{text: 'HTML/XML', value: 'markup'},
		{text: 'JavaScript', value: 'javascript'},
		{text: 'CSS', value: 'css'},
		{text: 'PHP', value: 'php'},
		{text: 'Ruby', value: 'ruby'},
		{text: 'Python', value: 'python'},
		{text: 'Java', value: 'java'},
		{text: 'C', value: 'c'},
		{text: 'C#', value: 'csharp'},
		{text: 'C++', value: 'cpp'},
		{text: 'Git', value: 'git'},
		{text: 'vim-script', value: 'vim'},
		{text: 'Elm-lang', value: 'elm'},
		{text: 'Django', value: 'django'},
		{text: 'SQL', value: 'sql'},
		{text: 'Ruby', value: 'ruby'},
		{text: 'Regex', value: 'regex'},
	],
  toolbar: 'undo redo | formatselect | ' +
  ' bold italic backcolor | alignleft aligncenter ' +
  ' alignright alignjustify | bullist numlist outdent indent |' +
  ' removeformat | help | codesample code image',
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tiny.cloud/css/codepen.min.css'
  ]
});

