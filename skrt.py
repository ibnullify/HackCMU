<form action="Loan.jsp" method="POST"><msp:evaluate>
		Get["Business`loanspecial`"]; 
		Get["Cluster`"];
	</msp:evaluate><table><tr><td><select name="Type" size="1"><option value="1" ${param.Type == '1' ? 'selected="selected"' : ''}>
						Principal
					</option><option value="2" ${param.Type == '2' ? 'selected="selected"' : ''}>
						Monthly Payment
					</option></select>
				= 
				<input type="Text" name="Amount" align="LEFT" size="6"
					value="${not empty param.Amount ? param.Amount : '10000' }" /><br /></td></tr><tr><td><strong>Period (years) = </strong><input type="TEXT" name="Period" align="LEFT" size="6"
					value="${not empty param.Period ? param.Period : '20' }" /><br /></td></tr><tr><td><strong>Rate = </strong><input type="TEXT" name="Rate" align="LEFT" size="6" 
					value="${not empty param.Rate ? param.Rate : '0.075' }" /><br /><br /></td></tr></table><br /><input type="image" src="../images/Template2/evaluate.gif" border="0"
		name="btnSubmit" value="Evaluate" alt="Evaluate" title="Evaluate" /></form><br /><br /><c:if test="${not empty param.Rate}"><div class="webm-results">Results</div><div style="padding: 5px; border: 13px solid #CCC; display: table-cell;"><msp:evaluate>
		MSPBlock[$$Type, 
			MSPFormatForCluster[Style[
				Which[$$Type === 1, "Your monthly payments would be $",
					$$Type === 2, "You can afford a loan amount of $", 
					True, Head[$$Type]], Bold], StandardForm]]
	</msp:evaluate><msp:evaluate>
		MSPBlock[{$$Type, $$Amount, $$Period, $$Rate},
			If[NumberQ[$$Amount]&&NumberQ[$$Period]&&NumberQ[$$Rate], 
				MSPFormatForCluster[Style[Figure[$$Type, $$Amount, $$Rate,$$Period], Bold], 
				StandardForm]]]
	</msp:evaluate></div></c:if>
